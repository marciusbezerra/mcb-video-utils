
from datetime import datetime
import subprocess
import platform
import sys
import os
import uuid
from PySide6.QtMultimedia import QMediaPlayer, QAudioOutput
from PySide6.QtMultimediaWidgets import QVideoWidget
from PySide6.QtWidgets import QApplication, QMainWindow, QFileDialog, QMessageBox, QProgressBar
from PySide6.QtGui import QStandardItem, QStandardItemModel
from PySide6.QtCore import QUrl, QSettings, QFileInfo, QTime
from mainwindow import Ui_MainWindow
import re

APP_CREDITS_ORGANIZATION = 'MCBMAX'
APP_CREDITS_NAME = 'MCBAutoEditorGUI'
APP_CREDITS_FRIENDLY_NAME = 'MCB AutoEditor GUI'
APP_CREDITS_VERSION = '1.0.0'
APP_CREDITS_DEV = 'Marcius Bezerra'

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

        self.player = QMediaPlayer(self)
        self.audioOutput = QAudioOutput(self)
        self.videoWidget = QVideoWidget(self.widgetPreview)
        self.videoWidget.setVisible(False)

        self.model = QStandardItemModel(self.listViewVideosIn)
        self.listViewVideosIn.setModel(self.model) 

        self.segmentsModel = QStandardItemModel(self.listViewSegments)
        self.listViewSegments.setModel(self.segmentsModel)

        self.toolButtonAddVideo.clicked.connect(self.open_file)
        self.pushButtonDeleteVideoIn.clicked.connect(self.remove_video)
        self.toolButtonMoveVideoUp.clicked.connect(self.move_video_up)
        self.toolButtonMoveVideoDown.clicked.connect(self.move_video_down)
        self.pushButtonProcess.clicked.connect(self.process_video)

        self.listViewVideosIn.selectionModel().selectionChanged.connect(self.update_ui)

        self.pushButtonStop.clicked.connect(self.stop_player)
        self.pushButtonBegin.clicked.connect(lambda: self.player.setPosition(0))
        self.pushButtonPrev10m.clicked.connect(lambda: self.player.setPosition(self.player.position() - 10 * 60 * 1000))
        self.pushButtonPrev1m.clicked.connect(lambda: self.player.setPosition(self.player.position() - 1 * 60 * 1000))
        self.pushButtonPrev10s.clicked.connect(lambda: self.player.setPosition(self.player.position() - 10 * 1000))
        self.pushButtonNext10s.clicked.connect(lambda: self.player.setPosition(self.player.position() + 10 * 1000))
        self.pushButtonNext1m.clicked.connect(lambda: self.player.setPosition(self.player.position() + 1 * 60 * 1000))
        self.pushButtonNext10m.clicked.connect(lambda: self.player.setPosition(self.player.position() + 10 * 60 * 1000))
        self.pushButtonEnd.clicked.connect(lambda: self.player.setPosition(self.player.duration()))

        self.pushButtonPlayPause.clicked.connect(self.toggle_play_pause)
        self.player.positionChanged.connect(self.update_video_time)

        self.toolButtonStartSegment.clicked.connect(lambda: self.toolButtonStartSegment.setText(str(int(self.player.position() / 1000))))
        self.toolButtonEndSegment.clicked.connect(lambda: self.toolButtonEndSegment.setText(str(int(self.player.position() / 1000))))

        self.toolButtonAddSegment.clicked.connect(lambda: self.segmentsModel.appendRow(QStandardItem(f'{self.toolButtonStartSegment.text()}sec,{self.toolButtonEndSegment.text()}sec')))
        self.toolButtonDeleteSegment.clicked.connect(lambda: self.segmentsModel.removeRow(self.listViewSegments.selectedIndexes()[0].row()))

        self.progress_bar = None

        self.connect_video_events()

    def resizeEvent(self, event):
        self.videoWidget.resize(self.widgetPreview.size())
        super().resizeEvent(event)

    def toggle_play_pause(self):
        if self.player.playbackState() == QMediaPlayer.PlayingState:
            self.player.pause()
            self.pushButtonPlayPause.setText('Play')
        else:
            self.player.play()
            self.pushButtonPlayPause.setText('Pause')

    def update_video_time(self, position):
        video_time = QTime.fromMSecsSinceStartOfDay(position)
        self.labelVideoTime.setText(video_time.toString('hh:mm:ss.zzz'))

    def open_file(self):
        settings = QSettings(APP_CREDITS_ORGANIZATION, APP_CREDITS_NAME) 
        dir_path = settings.value('last_open_dir', '')  
        file_dialog = QFileDialog(self)
        file_dialog.setDirectory(dir_path)
        file_dialog.setNameFilter('Video Files (*.mp4 *.avi *.mov *.mkv *.wmv)')
        file_dialog.selectNameFilter('Video Files (*.mp4 *.avi *.mov *.mkv *.wmv)')
        file_dialog.setViewMode(QFileDialog.Detail)
        file_dialog.setFileMode(QFileDialog.ExistingFile)
        file_dialog.setAcceptMode(QFileDialog.AcceptOpen)
        file_dialog.open()
        if file_dialog.exec() == QFileDialog.Accepted:
            file_path = file_dialog.selectedFiles()[0]
            dir_path = QFileInfo(file_path).absoluteDir().absolutePath() 
            settings.setValue('last_open_dir', dir_path)  
            video_file = VideoFile(file_path, True, 0, 0, [])

            item = QStandardItem(str(video_file))
            item.setData(video_file)
            self.model.appendRow(item)

    def remove_video(self):
        indexes = self.listViewVideosIn.selectedIndexes()
        if indexes:
            self.model.removeRow(indexes[0].row())

    def stop_player(self):
        self.player.stop()
        self.pushButtonPlayPause.setText('Play')
        self.labelVideoTime.setText('00:00:00.000')

    def update_ui(self):

        self.stop_player()

        self.disconnect_video_events()
        self.videoWidget.setVisible(False)
        try:
            indexes = self.listViewVideosIn.selectedIndexes()

            has_selection = len(indexes) > 0

            self.checkBoxEnableEdit.setEnabled(has_selection)
            self.spinBoxMinAudio.setEnabled(has_selection)
            self.spinBoxMinMotion.setEnabled(has_selection)
            self.pushButtonDeleteVideoIn.setEnabled(has_selection)
            self.toolButtonStartSegment.setEnabled(has_selection)
            self.toolButtonStartSegment.setText('[')
            self.toolButtonEndSegment.setEnabled(has_selection)
            self.toolButtonEndSegment.setText(']')
            self.toolButtonAddSegment.setEnabled(has_selection)
            self.toolButtonDeleteSegment.setEnabled(has_selection)
            self.listViewSegments.setEnabled(has_selection)

            self.pushButtonStop.setEnabled(has_selection)
            self.pushButtonBegin.setEnabled(has_selection)
            self.pushButtonPrev10m.setEnabled(has_selection)
            self.pushButtonPrev1m.setEnabled(has_selection)
            self.pushButtonPrev10s.setEnabled(has_selection)
            self.pushButtonNext10s.setEnabled(has_selection)
            self.pushButtonNext1m.setEnabled(has_selection)
            self.pushButtonNext10m.setEnabled(has_selection)
            self.pushButtonEnd.setEnabled(has_selection)
            self.pushButtonPlayPause.setEnabled(has_selection)

            if indexes:
                video = self.model.itemFromIndex(indexes[0]).data()

                self.checkBoxEnableEdit.setChecked(video.edit)
                self.spinBoxMinAudio.setValue(video.minAudio)
                self.spinBoxMinMotion.setValue(video.minMotion)

                self.segmentsModel.clear()
                for segment in video.exclude_segments:
                    item = QStandardItem(segment)
                    self.segmentsModel.appendRow(item)

                self.videoWidget.setVisible(True)
                self.videoWidget.resize(self.widgetPreview.size())
                self.player = QMediaPlayer(self)
                self.audioOutput = QAudioOutput(self)
                self.player.setAudioOutput(self.audioOutput)
                self.player.setVideoOutput(self.videoWidget)
                self.player.positionChanged.connect(self.update_video_time)
                self.player.setSource(QUrl.fromLocalFile(video.filename))
                self.audioOutput.setVolume(100)

        except Exception as identifier:
            QMessageBox.critical(self, 'Error', 'An error occurred while updating the UI: ' + str(identifier))
            pass
        finally:
            self.connect_video_events()

    def update_video(self):
        indexes = self.listViewVideosIn.selectedIndexes()
        if indexes:
            video = self.model.itemFromIndex(indexes[0]).data()
            video.edit = self.checkBoxEnableEdit.isChecked()
            video.minAudio = self.spinBoxMinAudio.value()
            video.minMotion = self.spinBoxMinMotion.value()
            
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

    def get_video_duration(self, filename):
        """Obtém a duração total do vídeo em segundos"""
        result = subprocess.run(
            ["ffprobe", "-v", "error", "-show_entries",
            "format=duration", "-of",
            "default=noprint_wrappers=1:nokey=1", filename],
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT)
        return float(result.stdout)
    
    def move_video_up(self):
        indexes = self.listViewVideosIn.selectedIndexes()
        if indexes:
            row = indexes[0].row()
            if row > 0:
                self.model.insertRow(row - 1, self.model.takeRow(row))
                self.listViewVideosIn.setCurrentIndex(self.model.index(row - 1, 0))
    
    def move_video_down(self):
        indexes = self.listViewVideosIn.selectedIndexes()
        if indexes:
            row = indexes[0].row()
            if row < self.model.rowCount() - 1:
                self.model.insertRow(row + 1, self.model.takeRow(row))
                self.listViewVideosIn.setCurrentIndex(self.model.index(row + 1, 0))
    
    def get_total_duration(self, filenames):
        """Calcula a duração total combinada de vários arquivos."""
        total_duration = sum(self.get_video_duration(filename) for filename in filenames)
        return total_duration

    def report_progress_percent(self, status_line, duration):
        print(status_line)
        if not self.progress_bar:
            self.progress_bar = QProgressBar()
            self.progress_bar.setRange(0, 100)
            self.progress_bar.setValue(0)
            self.statusBar().addPermanentWidget(self.progress_bar)

        if 'Creating new video' in status_line or 'Creating new audio' in status_line or 'Analyzing motion' in status_line:
            if not self.progress_bar.isVisible():
                self.progress_bar.show()
            status_msg = status_line.split('~')[0]
            self.statusBar().showMessage(status_msg)
            current = int(status_line.split('~')[1])
            total = int(status_line.split('~')[2])
            percent = int((current / total) * 100)
            self.progress_bar.setValue(percent)
        elif 'frame=' in status_line and 'fps=' in status_line and duration > 0:
            regex = re.compile(r"time=(\d{2}):(\d{2}):(\d{2})\.(\d{2})")
            match = regex.search(status_line)
            if match:
                if not self.progress_bar.isVisible():
                    self.progress_bar.show()
                self.statusBar().showMessage(status_line[:60])
                hours, minutes, seconds, _ = map(int, match.groups())
                current_time = hours * 3600 + minutes * 60 + seconds
                progress = (current_time / duration) * 100
                self.progress_bar.setValue(progress)
        else:
            if self.progress_bar.isVisible():
                self.progress_bar.hide()

    def run_command(self, command, duration = 0):
        print(command)
        process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)
        while True:
            output_line = process.stdout.readline()
            if output_line == '' and process.poll() is not None:
                break
            if output_line:
                self.report_progress_percent(output_line.strip(), duration)
        if process.returncode == 0:
            return True
        else:
            return False
        
    def deduce_output_filename(self):
        filename = f'{datetime.now().strftime("%Y_%m_%d_%H_%M_%S")}_processed.mp4'
        if self.model.rowCount() == 1:
            base_filename = QFileInfo(self.model.item(0).data().filename).baseName()
            ext = QFileInfo(self.model.item(0).data().filename).suffix()
            filename = f'{base_filename}_processed.{ext}'
        return filename
    
    def open_folder(self, path):
        if platform.system() == "Windows":
            os.startfile(path)
        elif platform.system() == "Darwin":
            subprocess.Popen(["open", path])
        else:
            subprocess.Popen(["xdg-open", path])

    def process_video(self):
        try:
            self.stop_player()
            if self.model.rowCount() == 0:
                QMessageBox.critical(self, 'Error', 'Nenhum vídeo para processar!')
                return
            
            settings = QSettings(APP_CREDITS_ORGANIZATION, APP_CREDITS_NAME)  
            last_path = settings.value('last_save_dir', '')  
            default_filename = self.deduce_output_filename()
            outFilename = QFileDialog.getSaveFileName(self, 'Salvar Arquivo', f'{last_path}/{default_filename}', 'Video Files (*.mp4)')

            if not outFilename[0]:
                return
            
            out_path = QFileInfo(outFilename[0]).absoluteDir().absolutePath()
            files_to_join = []

            for i in range(self.model.rowCount()):
                audio_motion_config = ''
                video = self.model.item(i).data()
                if video.edit:
                    auto_editor_command = ['auto-editor']
                    auto_editor_command.append(video.filename)
                    hasAudioMotionConfig = video.minAudio > 0 or video.minMotion > 0
                    if hasAudioMotionConfig:
                        auto_editor_command.append('--edit')
                        audio_motion_config += '(or'
                    if video.minAudio > 0:
                        audio_motion_config += f' audio:{video.minAudio}%'
                    if video.minMotion > 0:
                        audio_motion_config += f' motion:{video.minMotion}%'
                    if hasAudioMotionConfig:
                        audio_motion_config += ')'
                        auto_editor_command.append(audio_motion_config)
                    if video.exclude_segments:
                        auto_editor_command.append('--add-in')
                        auto_editor_command += video.exclude_segments

                    tmpFilename = f'{out_path}/{uuid.uuid4()}.mp4'

                    auto_editor_command.append('--output')
                    auto_editor_command.append(tmpFilename)
                    auto_editor_command.append('--no-open')
                    auto_editor_command.append('--progress')
                    auto_editor_command.append('machine') 
                    
                    files_to_join.append(tmpFilename)
                    if not self.run_command(auto_editor_command):
                        QMessageBox.critical(self, 'Error', 'An error occurred while processing the video!')
                        return
                else:
                    files_to_join.append(video.filename)

            ffmpeg_command = ['ffmpeg']
            for i in range(len(files_to_join)):
                inFilename = files_to_join[i]
                ffmpeg_command.append('-i')
                ffmpeg_command.append(inFilename)

            video_total_duration = self.get_total_duration(files_to_join)

            has_complex_filter = len(files_to_join) > 1
            
            if has_complex_filter:
                filter_complex = ''
                ffmpeg_command.append('-filter_complex')
                for i in range(len(files_to_join)):
                    filter_complex += f'[{i}:v][{i}:a]'
                filter_complex += f'concat=n={self.model.rowCount()}:v=1:a=1[outv][outa]'
                if self.checkBoxEnableVideoConv.isChecked():
                    filter_complex += f';[outv]fps={self.spinBoxVideoFps.value()}[outv]'
                ffmpeg_command.append(filter_complex)
                ffmpeg_command.append('-map')
                ffmpeg_command.append('[outv]')
                ffmpeg_command.append('-map')
                ffmpeg_command.append('[outa]')

            if self.checkBoxEnableVideoConv.isChecked():
                ffmpeg_command.append('-c:v')
                ffmpeg_command.append(self.lineEditVideoCodec.text())
                ffmpeg_command.append('-crf')
                ffmpeg_command.append(str(self.spinBoxVideoCrf.value()))
                if not has_complex_filter:
                    ffmpeg_command.append('-filter:v')
                    ffmpeg_command.append(f'fps={self.spinBoxVideoFps.value()}')
            if self.checkBoxEnableAudioConv.isChecked():
                ffmpeg_command.append('-c:a')
                ffmpeg_command.append(self.lineEditAudioCodec.text())
                ffmpeg_command.append('-b:a')
                ffmpeg_command.append(f'{self.spinBoxAudioBitrate.value()}k')

            ffmpeg_command.append('-y')
            ffmpeg_command.append('-hide_banner')
            ffmpeg_command.append(outFilename[0])

            self.run_command(ffmpeg_command, video_total_duration)
            for file in files_to_join:
                os.remove(file)
                
            self.statusBar().showMessage('Vídeos processados com sucesso!')
            QMessageBox.information(self, 'Processamento', 'Vídeos processados com sucesso!')
            self.progress_bar.hide()
            settings.setValue('last_save_dir', out_path)
            self.open_folder(out_path)
        except Exception as e:
            QMessageBox.critical(self, 'Error', f'Ocorreu um erro: {e}')
        finally:
            for file in files_to_join:
                try:
                    os.remove(file)
                except OSError:
                    pass

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())