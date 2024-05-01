
import sys
from PySide6.QtMultimedia import QMediaPlayer, QAudioOutput
from PySide6.QtMultimediaWidgets import QVideoWidget
from PySide6.QtWidgets import QApplication, QMainWindow, QFileDialog, QMessageBox
from PySide6.QtGui import QStandardItem, QStandardItemModel
from PySide6.QtCore import QUrl
from mainwindow import Ui_MainWindow

class VideoFile:
    def __init__(self, filename, edit, minAudio, minMotion, exclude_segments):
        self.filename = filename
        self.edit = edit
        self.minAudio = minAudio
        self.minMotion = minMotion
        self.exclude_segments = exclude_segments

    def __str__(self):
        return self.filename

class MainWindow(QMainWindow, Ui_MainWindow):

    def __init__(self):
        super().__init__()
        self.setupUi(self)

        # Create a QMediaPlayer and a QVideoWidget
        self.player = QMediaPlayer(self)
        self.audioOutput = QAudioOutput(self)
        self.videoWidget = QVideoWidget(self.widgetPreview)
        self.videoWidget.setVisible(False)

        self.model = QStandardItemModel(self.listViewVideosIn)
        self.listViewVideosIn.setModel(self.model) 

        self.segmentsModel = QStandardItemModel(self.listViewSegments)
        self.listViewSegments.setModel(self.segmentsModel)

        self.toolButtonOpenFile.clicked.connect(self.open_file)
        self.pushButtonDeleteVideoIn.clicked.connect(self.remove_video)

        self.listViewVideosIn.selectionModel().selectionChanged.connect(self.update_ui)

        self.connect_video_events()

    def resizeEvent(self, event):
        # Resize the QVideoWidget when the window is resized
        self.videoWidget.resize(self.widgetPreview.size())
        super().resizeEvent(event)

    def open_file(self):
        file_dialog = QFileDialog(self)
        file_dialog.setNameFilter('Video Files (*.mp4 *.avi *.mov *.mkv *.wmv)')
        file_dialog.selectNameFilter('Video Files (*.mp4 *.avi *.mov *.mkv *.wmv)')
        file_dialog.setViewMode(QFileDialog.Detail)
        file_dialog.setFileMode(QFileDialog.ExistingFile)
        file_dialog.setAcceptMode(QFileDialog.AcceptOpen)
        file_dialog.open()
        if file_dialog.exec() == QFileDialog.Accepted:
            file_path = file_dialog.selectedFiles()[0]
            self.lineEditVideoIn.setText(file_path)
            video_file = VideoFile(file_path, True, 0, 0, [])

            item = QStandardItem(str(video_file))
            item.setData(video_file)
            self.model.appendRow(item)

    def remove_video(self):
        indexes = self.listViewVideosIn.selectedIndexes()
        if indexes:
            self.model.removeRow(indexes[0].row())

    def update_ui(self):

        self.disconnect_video_events()
        self.videoWidget.setVisible(False)
        try:
            # Get the currently selected VideoFile
            indexes = self.listViewVideosIn.selectedIndexes()
            if indexes:
                video = self.model.itemFromIndex(indexes[0]).data()

                # Update the UI elements
                self.checkBoxEnableEdit.setChecked(video.edit)
                self.spinBoxMinAudio.setValue(video.minAudio)
                self.spinBoxMinMotion.setValue(video.minMotion)

                # Update the listViewSegments
                self.segmentsModel.clear()
                for segment in video.exclude_segments:
                    item = QStandardItem(segment)
                    self.segmentsModel.appendRow(item)

                # Set the QVideoWidget as the video output of the QMediaPlayer
                self.player.stop()
                self.videoWidget.setVisible(True)
                self.player.setVideoOutput(self.videoWidget)
                self.videoWidget.resize(self.widgetPreview.size())
                self.player.setSource(QUrl.fromLocalFile(video.filename))
                self.audioOutput.setVolume(100)
                self.player.setAudioOutput(self.audioOutput)
                self.player.play()
                

        except Exception as identifier:
            QMessageBox.critical(self, 'Error', 'An error occurred while updating the UI: ' + str(identifier))
            pass
        finally:
            self.connect_video_events()

    def update_video(self):
        # Get the currently selected VideoFile
        indexes = self.listViewVideosIn.selectedIndexes()
        if indexes:
            video = self.model.itemFromIndex(indexes[0]).data()
            print(video)

            video.edit = self.checkBoxEnableEdit.isChecked()
            video.minAudio = self.spinBoxMinAudio.value()
            video.minMotion = self.spinBoxMinMotion.value()
            
            # Update the exclude_segments list
            video.exclude_segments = [self.segmentsModel.item(i).text() for i in range(self.segmentsModel.rowCount())]

    def connect_video_events(self):
        self.checkBoxEnableEdit.stateChanged.connect(self.update_video)
        self.spinBoxMinAudio.valueChanged.connect(self.update_video)
        self.spinBoxMinMotion.valueChanged.connect(self.update_video)
        self.listViewSegments.model().rowsInserted.connect(self.update_video)
        self.listViewSegments.model().rowsRemoved.connect(self.update_video)

    def disconnect_video_events(self):
        self.checkBoxEnableEdit.stateChanged.disconnect(self.update_video)
        self.spinBoxMinAudio.valueChanged.disconnect(self.update_video)
        self.spinBoxMinMotion.valueChanged.disconnect(self.update_video)
        self.listViewSegments.model().rowsInserted.disconnect(self.update_video)
        self.listViewSegments.model().rowsRemoved.disconnect(self.update_video)
    

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())