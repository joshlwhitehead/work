import csv
from datetime import datetime
import matplotlib.pyplot as plt
import os
import shutil
import pandas as pd
import numpy as np
import pathlib
from PyQt5 import QtWidgets
from PyQt5 import QtCore
from PyQt5.QtWidgets import QDialog

try:
    from Built_UI_Files.dave_window import Ui_dave_window
    from custom_libraries import DaveParsFuncs
except:
    pass

try:
    from dave_widget import Ui_dave_window
    import DaveParsFuncs
except:
    pass
date = '23Sep2022'





TEMP_CONSOLE_FILE_NAME = "console_output.txt"
LOCAL_TEST_DATA_FOLDER_NAME = "data"
AUTO_DAVE_OUTPUT_FOLDER_NAME = "auto_dave_output_files"

directory = ''.join([LOCAL_TEST_DATA_FOLDER_NAME,'/',date])
folder = os.path.isdir(directory)
if folder == True:
    pass
else:
    os.mkdir(directory)
timestamps = []

class Dave_Window(Ui_dave_window, QtWidgets.QWidget):
    console_signal = QtCore.pyqtSignal()
    console_read_signal = QtCore.pyqtSignal()

    def __init__(self, connected: False):
        super().__init__()
        self.setupUi(self)

        self.create_test_data_folder()
        self.checked = dict()
        self.current_checked = []
        self.dave = Dave(self)
        self.active_graphs = []
        self.active_values = []
        self.file_num = 1
        self.file_num_box.setValue(self.file_num)
        self.graph_selection_tree.clear()
        self.updateplots()
        self.setup_buttons()
        self.console_button_frame.setEnabled(False)

        if connected:
            self.console_read_signal.connect(self.read_console_data)

        # if not connected to RCade
        if not connected:
            self.graph_from_console_button.setVisible(False)
            self.graph_from_file_button.setVisible(False)
            self.data_source_line1.setVisible(False)
            self.console_button_frame.setVisible(False)
            self.log_file_name_label.setVisible(False)

    def setup_buttons(self):
        self.log_sel_btn.clicked.connect(self.getfile)
        self.log_file_out.setText(self.dave.filename)
        self.gen_graph_btn.clicked.connect(self.gengraph)
        self.graph_from_console_button.clicked.connect(self.graph_from_console_button_clicked)
        self.graph_from_file_button.clicked.connect(self.graph_from_file_button_clicked)
        self.write_log_to_file_button.clicked.connect(self.write_log_to_file_button_clicked)
        self.read_console_data_button.clicked.connect(self.emit_to_rcade_read_console_data_button_clicked)
        self.write_clean_csv_button.clicked.connect(self.write_clean_csv_button_clicked)
        self.graph_selection_tree.clicked.connect(self.updateSelectionTree)
        self.autoDave_Button.clicked.connect(self.dave.autoProcessData)

    # update the checkbox tree to contain plots that are in the selected data
    def updateplots(self):
        for plot in self.dave.plots:
            plot.setActive(False)
            item = QtWidgets.QTreeWidgetItem(self.graph_selection_tree)
            item.setText(0, plot.name)
            item.setCheckState(0, QtCore.Qt.Checked)
            self.graph_selection_tree.addTopLevelItem(item)
            row = []
            for parsedValue in plot.parsedValues:
                child_item = QtWidgets.QTreeWidgetItem(item)
                child_item.setText(0, parsedValue.name)
                child_item.setCheckState(0, QtCore.Qt.Checked)
                item.addChild(child_item)
                row.append(QtCore.Qt.Checked)
            self.current_checked.append(row)

    def create_tree_from_list(self, plots):
        self.graph_selection_tree.clear()
        num_plots = len(plots)
        for plot in plots:
            item = QtWidgets.QTreeWidgetItem(self.graph_selection_tree)
            item.setText(0, plot[0])
            if num_plots < 3:
                item.setCheckState(0, QtCore.Qt.Checked)
                item.setExpanded(True)
            else:
                item.setCheckState(0, QtCore.Qt.Unchecked)
            self.graph_selection_tree.addTopLevelItem(item)
            sub_value = plot[1]
            for value in sub_value:
                child_item = QtWidgets.QTreeWidgetItem(item)
                child_item.setText(0, value)
                if num_plots < 3:
                    child_item.setCheckState(0, QtCore.Qt.Checked)
                else:
                    child_item.setCheckState(0, QtCore.Qt.Unchecked)
                item.addChild(child_item)

    def get_possible_plots(self):
        checked = []
        for plot in self.dave.plots:
            plot_list = []
            plot_children_list = []
            for sub_value in plot.parsedValues:
                len_dict = len(sub_value.values)
                if len_dict != 0:
                    plot_children_list.append(sub_value.name)
            if len(plot_children_list) != 0:
                plot_list.append(plot.name)
                plot_list.append(plot_children_list)
                checked.append(plot_list)
        return checked

    def read_file(self):
        self.clear_dave_values()
        self.dave.parseLogFile(self.dave.fullPath)
        # possible_plots = self.get_possible_plots()
        # self.create_tree_from_list(possible_plots)

    def disable_graph_data_frame_section(self):
        self.gen_graph_btn.setDisabled(True)
        self.write_clean_csv_button.setDisabled(True)

    def enable_graph_data_frame_section(self):
        self.gen_graph_btn.setDisabled(False)
        self.write_clean_csv_button.setDisabled(False)

    # Creates a local_test_data_folder if not there.
    def create_test_data_folder(self):
        check_folder = os.path.isdir(LOCAL_TEST_DATA_FOLDER_NAME)

        # If folder doesn't exist, then create it.
        if not check_folder:
            os.makedirs(LOCAL_TEST_DATA_FOLDER_NAME)

    def write_log_to_file_button_clicked(self):
        file_name = ""
        file_name += self.file_name_box.text()
        file_name += self.file_num_box.text()
        file_name += ".txt"

        file_path = "./" + LOCAL_TEST_DATA_FOLDER_NAME + "/" + file_name

        shutil.copy(TEMP_CONSOLE_FILE_NAME, file_path)

        self.file_num_box.setValue(self.file_num_box.value() + 1)

    def write_clean_csv_button_clicked(self):
        check_folder = os.path.isdir(LOCAL_TEST_DATA_FOLDER_NAME)

        # If folder doesn't exist, then create it.
        if not check_folder:
            os.makedirs(LOCAL_TEST_DATA_FOLDER_NAME)

        file_name = ""
        file_name += self.csv_file_name_box.text()
        file_name += ".csv"

        file_path = "./" + LOCAL_TEST_DATA_FOLDER_NAME + "/" + date + "/" + file_name

        columns = ["timeSinceBoot"]
        dicts = []

        for graph in self.dave.plots:
            if graph.active:
                for val in graph.parsedValues:
                    if val.active:
                        columns.append(val.name)
                        dicts.append(val.values)

        timestamps = self.gettimestamps(dicts)

        with open(file_path, mode='w', ) as csv_file:
            csv_writer = csv.writer(csv_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL,
                                    lineterminator="\n")
            csv_writer.writerow(columns)
            for timestamp in timestamps:
                row = [timestamp]
                foundAnyAtTimestamp = False
                for d in dicts:
                    try:
                        row += [d[timestamp]]
                        foundAnyAtTimestamp = True
                    except:
                        row += ['']
                if foundAnyAtTimestamp:
                    csv_writer.writerow(row)

            csv_file.close()

    def gettimestamps(self, dicts):
        stamps = []
        for d in dicts:
            for key in d.keys():
                stamps.append(key)

        stamps.sort()
        return stamps

    def graph_from_console_button_clicked(self):
        self.console_button_frame.setEnabled(True)
        self.log_file_button_frame.setEnabled(False)

    def graph_from_file_button_clicked(self):
        self.console_button_frame.setEnabled(False)
        self.log_file_button_frame.setEnabled(True)

    # def read_console_data_button_clicked(self):
    #     //self.console_signal.emit()

    def emit_to_rcade_read_console_data_button_clicked(self):
        self.console_signal.emit()

    def read_console_data(self):
        self.log_file_out.setText(TEMP_CONSOLE_FILE_NAME)
        self.dave.filename = TEMP_CONSOLE_FILE_NAME

        path = pathlib.Path().resolve()
        data_folder = pathlib.Path(str(path))
        full_path = data_folder / TEMP_CONSOLE_FILE_NAME

        self.dave.fullPath = full_path
        self.read_file()

    # update the selection tree based off clicks
    def updateSelectionTree(self):
        root = self.graph_selection_tree.invisibleRootItem()
        signal_count = root.childCount()
        for i in range(signal_count):
            signal = root.child(i)
            child_box_clicked = False

            # checks parent box if child is selected
            if signal.checkState(0) != QtCore.Qt.Checked and self.current_checked[i][0] != QtCore.Qt.Checked:
                for n in range(signal.childCount()):
                    if signal.child(n).checkState(0) == QtCore.Qt.Checked:
                        signal.setCheckState(0, QtCore.Qt.Checked)
                        self.current_checked[i][0] = QtCore.Qt.Checked
                        child_box_clicked = True
                        break

            if signal.checkState(0) == self.current_checked[i][0]:  # if no state chane
                continue
            elif signal.checkState(0) == QtCore.Qt.Checked:
                self.current_checked[i][0] = QtCore.Qt.Checked
                selected = QtCore.Qt.Checked
            else:
                selected = QtCore.Qt.Unchecked
                self.current_checked[i][0] = QtCore.Qt.Unchecked

            if not child_box_clicked:  # flips all child boxes when parent is changed
                for n in range(signal.childCount()):
                    child = signal.child(n)
                    child.setCheckState(0, selected)

    # look through the checkbox tree and determine which values are checked, updating the checked dict accordingly
    def find_checked(self):
        self.checked = dict()
        root = self.graph_selection_tree.invisibleRootItem()
        signal_count = root.childCount()
        for i in range(signal_count):
            signal = root.child(i)
            if signal.checkState(0) == QtCore.Qt.Checked:
                checked_sweeps = list()
                num_children = signal.childCount()

                for n in range(num_children):
                    child = signal.child(n)

                    if child.checkState(0) == QtCore.Qt.Checked:
                        checked_sweeps.append(child.text(0))
                self.checked[signal.text(0)] = checked_sweeps
        # print(self.checked)

    # update the graphs that need to be plotted, then use the dave tool to plot them
    def gengraph(self):
        try:
            self.find_checked()
            self.activategraphsandplots()
            self.update_graphs_values()
            if self.dave.filename != "":
                self.dave.parseLogFile(self.dave.fullPath)
            self.dave.RunPlot()

        except:
            # self.console_print("Unable to Graph Data")
            pass

    # clear the active graphs and active values lists, then,
    # for every graph in the checked list that is selected, place it in the active graphs list
    # and for every value that is checked place it in the active values list
    def activategraphsandplots(self):
        self.active_graphs = []
        self.active_values = []
        for graph in self.checked.keys():
            self.active_graphs.append(str(graph))
        for value in self.checked.values():
            for name in value:
                self.active_values.append(str(name))

    # iterate through the dave.plots, and make sure that every graph
    # and value is set correctly to active or not by checking the active graphs
    # and values list.
    def update_graphs_values(self):
        for graph in self.dave.plots:
            graph.setActive(False)
            for val in graph.parsedValues:
                if len(val.values) > 10 and val.name in self.active_values:  # is there actually data?
                    graph.setActive(True)
                    val.setActive(True)
                else:
                    val.setActive(False)

    def getfile(self):
        success = self.dave.pickFile()

        if not success:
            return

        self.log_file_out.setText(self.dave.filename)
        self.enable_graph_data_frame_section()
        self.read_file()

    def clear_dave_values(self):
        for plot in self.dave.plots:
            for sub_values in plot.parsedValues:
                sub_values.values.clear()


class ParsedValue():
    def __init__(self, name, color, parseValueFunc=None, filterValueFunc=None, mainY=True, step=False, linewidth=1.0):
        self.name = name
        self.mainY = mainY
        self.color = color
        self.step = step
        self.line_width = linewidth
        self.filterValueFunc = filterValueFunc
        self.parseValueFunc = parseValueFunc
        self.values = {}
        self.ax = None
        self.active = True

    def setActive(self, active=True):
        self.active = active


class PlotGroup():
    def __init__(self, name):
        self.name = name
        self.active = True
        self.parsedValues = []

    def addParsedValue(self, parsedValue):
        self.parsedValues.append(parsedValue)

    def setActive(self, active=True):
        self.active = active


def wavelength_to_rgb(wavelength, gamma=0.8):
    ''' taken from http://www.noah.org/wiki/Wavelength_to_RGB_in_Python
    This converts a given wavelength of light to an
    approximate RGB color value. The wavelength must be given
    in nanometers in the range from 380 nm through 750 nm
    (789 THz through 400 THz).

    Based on code by Dan Bruton
    http://www.physics.sfasu.edu/astro/color/spectra.html
    Additionally alpha value set to 0.5 outside range
    '''
    wavelength = float(wavelength)
    if wavelength >= 380 and wavelength <= 750:
        A = 1.
    else:
        A = 0.5
    if wavelength < 380:
        wavelength = 380.
    if wavelength > 750:
        wavelength = 750.
    if wavelength >= 380 and wavelength <= 440:
        attenuation = 0.3 + 0.7 * (wavelength - 380) / (440 - 380)
        R = ((-(wavelength - 440) / (440 - 380)) * attenuation) ** gamma
        G = 0.0
        B = (1.0 * attenuation) ** gamma
    elif wavelength >= 440 and wavelength <= 490:
        R = 0.0
        G = ((wavelength - 440) / (490 - 440)) ** gamma
        B = 1.0
    elif wavelength >= 490 and wavelength <= 510:
        R = 0.0
        G = 1.0
        B = (-(wavelength - 510) / (510 - 490)) ** gamma
    elif wavelength >= 510 and wavelength <= 580:
        R = ((wavelength - 510) / (580 - 510)) ** gamma
        G = 1.0
        B = 0.0
    elif wavelength >= 580 and wavelength <= 645:
        R = 1.0
        G = (-(wavelength - 645) / (645 - 580)) ** gamma
        B = 0.0
    elif wavelength >= 645 and wavelength <= 750:
        attenuation = 0.3 + 0.7 * (750 - wavelength) / (750 - 645)
        R = (1.0 * attenuation) ** gamma
        G = 0.0
        B = 0.0
    else:
        R = 0.0
        G = 0.0
        B = 0.0
    return (R, G, B, A)


def NewSubplot(singlePlot, axs, index, parsedValue):
    if singlePlot:
        obj = axs
    else:
        obj = axs[index]
    lists = sorted(parsedValue.values.items())
    if len(lists) >= 2:
        x, y = zip(*lists)

        if parsedValue.step:
            obj.step(x, y, where='post', color=parsedValue.color, label=parsedValue.name,
                     linewidth=parsedValue.line_width)
        else:
            obj.plot(x, y, color=parsedValue.color, label=parsedValue.name, linewidth=parsedValue.line_width,
                     clip_on=False)
        obj.tick_params(axis='y', labelcolor=parsedValue.color)


def AddToSubplotWithNewY(singlePlot, axs, index, parsedValue, newYIndex):
    if singlePlot:
        obj = axs
    else:
        obj = axs[index]
    if parsedValue.ax != None:
        parsedValue.ax.cla()
    ax = obj.twinx()
    parsedValue.ax = ax
    lists = sorted(parsedValue.values.items())
    if len(lists) >= 2:
        x, y = zip(*lists)
        ax.set_ylabel(parsedValue.name, color=parsedValue.color)
        if parsedValue.step:
            ax.step(x, y, where='post', color=parsedValue.color, label=parsedValue.name,
                    linewidth=parsedValue.line_width, clip_on=False)
        else:
            ax.plot(x, y, color=parsedValue.color, label=parsedValue.name, linewidth=parsedValue.line_width,
                    clip_on=False)

        ax.spines['right'].set_position(('outward', 40 * newYIndex))

        ax.tick_params(axis='y', labelcolor=parsedValue.color)


def AddToSubplot(singlePlot, axs, index, parsedValue):
    if singlePlot:
        obj = axs
    else:
        obj = axs[index]
    lists = sorted(parsedValue.values.items())
    if len(lists) >= 2:
        x, y = zip(*lists)
        if parsedValue.step:
            obj.step(x, y, where='post', color=parsedValue.color, label=parsedValue.name,
                     linewidth=parsedValue.line_width, clip_on=False)
        else:
            obj.plot(x, y, color=parsedValue.color, label=parsedValue.name, linewidth=parsedValue.line_width,
                     clip_on=False)


class Dave:
    def __init__(self, myWidget, MAXPLOTS=8):
        self.parent = myWidget
        self.MAXPLOTS = MAXPLOTS
        self.fullPath = ""
        self.filename = ""
        self.dlFullPath = ""
        self.dlFilename = ""
        self.totalData = pd.DataFrame()

        self.stage1Plot = PlotGroup("Stage1")
        self.stage1Plot.addParsedValue(
            ParsedValue("Stage1 TempC", color='tab:cyan', parseValueFunc=DaveParsFuncs.stage1TempCFunc))

        self.stage1Plot.addParsedValue(
            ParsedValue("Stage1 Modeled TempC", color='tab:red', parseValueFunc=DaveParsFuncs.stage1ModeledTempCFunc))

        self.stage1Plot.addParsedValue(
            ParsedValue("Stage1 Expected TempC", color='tab:orange', parseValueFunc=DaveParsFuncs.stage1ExpectedTempCFunc))

        self.stage1Plot.addParsedValue(
            ParsedValue("Stage1 Target TempC", color='tab:green', parseValueFunc=DaveParsFuncs.stage1TargetTempCFunc, step=True))

        self.stage1Plot.addParsedValue(
            ParsedValue("Stage1 Controlled Ramp Target", color='tab:blue', parseValueFunc=DaveParsFuncs.stage1ControlledRampTargetFunc, step=True))

        self.stage1Plot.addParsedValue(
            ParsedValue("Stage1 Thermocouple TempC", color='tab:blue', parseValueFunc=DaveParsFuncs.measuredStg1TempC))
        self.stage1Plot.addParsedValue(
            ParsedValue("Stage1 Thermocouple TempC 2", color='tab:purple', parseValueFunc=DaveParsFuncs.measuredStg1TempC2))
        self.stage1Plot.addParsedValue(
            ParsedValue("Stage1 Thermocouple TempC 3", color='tab:red', parseValueFunc=DaveParsFuncs.measuredStg1TempC3))

        self.stage1Plot.addParsedValue(
            ParsedValue("Stage1 Heatsink", color='tab:grey', parseValueFunc=DaveParsFuncs.stage1HeatSinkTempFunc))

        # self.stage1Plot.addParsedValue(
        #     ParsedValue("DataQ Stg1 Heatsink", color='tab:gray', parseValueFunc=ParsFuncs.dataQStage1Heatsink))
        # self.stage1Plot.addParsedValue(
        #     ParsedValue("dataQStg1PeltierTop", color='tab:pink', parseValueFunc=ParsFuncs.dataQC1T))
        # self.stage1Plot.addParsedValue(
        #     ParsedValue("dataQStage1PeltierBottom", color='tab:olive', parseValueFunc=ParsFuncs.dataQC1B))

        self.stage1OutputPlot = PlotGroup("Stage1 Output")

        self.stage1OutputPlot.addParsedValue(
            ParsedValue("Stage1 Output", color='tab:orange', parseValueFunc=DaveParsFuncs.stage1OutputFunc, mainY=False))

        self.stage1OutputPlot.addParsedValue(
            ParsedValue("Stage1 Actual TEC Temp Rate", color='tab:olive', parseValueFunc=DaveParsFuncs.stage1ActualTecRampRateFunc))


        self.pcrPlot = PlotGroup("Pcr")

        self.pcrPlot.addParsedValue(
            ParsedValue("PCR Temp", color='tab:cyan', parseValueFunc=DaveParsFuncs.pcrTempCFunc))

        self.pcrPlot.addParsedValue(
            ParsedValue("PCR Modeled TempC", color='tab:orange', parseValueFunc=DaveParsFuncs.pcrModeledTempCFunc))

        self.pcrPlot.addParsedValue(
            ParsedValue("PCR Expected TempC", color='tab:green', parseValueFunc=DaveParsFuncs.pcrExpectedTempCFunc,step=True))

        self.pcrPlot.addParsedValue(
            ParsedValue("PCR Target TempC", color='tab:pink', parseValueFunc=DaveParsFuncs.pcrTargetTempCFunc,step=True))

        self.pcrPlot.addParsedValue(
            ParsedValue("PCR Controlled Ramp Target", color='tab:red', parseValueFunc=DaveParsFuncs.pcrControlledRampTargetFunc))

        self.pcrPlot.addParsedValue(
            ParsedValue("PCR Thermocouple TempC", color='tab:blue', parseValueFunc=DaveParsFuncs.measuredPcrTempC))

        self.pcrPlot.addParsedValue(
            ParsedValue("PCR HeatSink TempC", color='tab:grey', parseValueFunc=DaveParsFuncs.pcrHeatSinkTempFunc))
        # self.pcrPlot.addParsedValue(
        #     ParsedValue("DataQ Pcr Heatsink", color='tab:green', parseValueFunc=ParsFuncs.dataQPcrHeatsink))
        # self.pcrPlot.addParsedValue(ParsedValue("Raw TEC Model", color='tab:blue', parseValueFunc=ParsFuncs.rawTECModel))
        # self.pcrPlot.addParsedValue(
        #     ParsedValue("DataQ Pcr Peltier Top", color='tab:pink', parseValueFunc=ParsFuncs.dataQPCRT))
        # self.pcrPlot.addParsedValue(
        #     ParsedValue("DataQ Pcr Peltier Bottom", color='tab:cyan', parseValueFunc=ParsFuncs.dataQPCRB))

        self.pcrOutputPlot = PlotGroup("Pcr Output")
        self.pcrOutputPlot.addParsedValue(
            ParsedValue("PCR Output", color='tab:orange', parseValueFunc=DaveParsFuncs.pcrOutputFunc, mainY=False))

        # self.motorsPlot = PlotGroup("Motors")
        # self.motorsPlot.addParsedValue(ParsedValue("Plunge Motor", color='tab:red', parseValueFunc=motorPlungeFunc))
        # self.motorsPlot.addParsedValue(ParsedValue("Latch Motor", color='tab:green', parseValueFunc=motorLatchFunc))

        errorMsPlot = PlotGroup("ErrorMs")
        errorMsPlot.addParsedValue(
            ParsedValue("Stage1 Error Time Ms", color='tab:red', parseValueFunc=DaveParsFuncs.stage1ErrorTimeMs))
        errorMsPlot.addParsedValue(
            ParsedValue("PCR Error Time Ms", color='tab:blue', parseValueFunc=DaveParsFuncs.pcrErrorTimeMs))

        ratesPlot = PlotGroup("Rates")
        ratesPlot.addParsedValue(
            ParsedValue("Stage1 Target Rate", color='tab:cyan', parseValueFunc=DaveParsFuncs.stage1TargetRate))
        ratesPlot.addParsedValue(
            ParsedValue("Stage1 TEC Rate", color='tab:red', parseValueFunc=DaveParsFuncs.stage1TecRate))
        ratesPlot.addParsedValue(
            ParsedValue("Stage1 Heatsink Rate", color='tab:orange', parseValueFunc=DaveParsFuncs.stage1HeatsinkRate))

        ratesPlot.addParsedValue(
            ParsedValue("PCR Target Rate", color='tab:brown', parseValueFunc=DaveParsFuncs.pcrTargetRate))
        ratesPlot.addParsedValue(
            ParsedValue("PCR TEC Rate", color='tab:purple', parseValueFunc=DaveParsFuncs.pcrTecRate))
        ratesPlot.addParsedValue(
            ParsedValue("PCR Heatsink Rate", color='tab:pink', parseValueFunc=DaveParsFuncs.pcrHeatsinkRate))

        self.fluorescencePlot = PlotGroup("Color Sensor")
        self.fluorescencePlot.addParsedValue(
            ParsedValue("415nm", color=wavelength_to_rgb(415), parseValueFunc=DaveParsFuncs.fluorescenceFunc0))
        self.fluorescencePlot.addParsedValue(
            ParsedValue("445nm", color=wavelength_to_rgb(445), parseValueFunc=DaveParsFuncs.fluorescenceFunc1))
        self.fluorescencePlot.addParsedValue(
            ParsedValue("480nm", color=wavelength_to_rgb(480), parseValueFunc=DaveParsFuncs.fluorescenceFunc2))
        self.fluorescencePlot.addParsedValue(
            ParsedValue("515nm", color=wavelength_to_rgb(515), parseValueFunc=DaveParsFuncs.fluorescenceFunc3))
        self.fluorescencePlot.addParsedValue(
            ParsedValue("555nm", color=wavelength_to_rgb(555), parseValueFunc=DaveParsFuncs.fluorescenceFunc4))
        self.fluorescencePlot.addParsedValue(
            ParsedValue("590nm", color=wavelength_to_rgb(590), parseValueFunc=DaveParsFuncs.fluorescenceFunc5))
        self.fluorescencePlot.addParsedValue(
            ParsedValue("630nm", color=wavelength_to_rgb(630), parseValueFunc=DaveParsFuncs.fluorescenceFunc6))
        self.fluorescencePlot.addParsedValue(
            ParsedValue("680nm", color=wavelength_to_rgb(680), parseValueFunc=DaveParsFuncs.fluorescenceFunc7))
        self.fluorescencePlot.addParsedValue(
            ParsedValue("Clear", color='tab:gray', parseValueFunc=DaveParsFuncs.fluorescenceFunc8))
        self.fluorescencePlot.addParsedValue(
            ParsedValue("Nir", color=wavelength_to_rgb(720), parseValueFunc=DaveParsFuncs.fluorescenceFunc9))
        self.fluorescencePlot.addParsedValue(
            ParsedValue("QDotRatio", color='tab:brown', parseValueFunc=DaveParsFuncs.qDotRatioFunc))
        self.fluorescencePlot.addParsedValue(
            ParsedValue("FluorTemp", color='tab:brown', parseValueFunc=DaveParsFuncs.fluorescenceFuncTemp))
        self.fluorescencePlot.addParsedValue(
            ParsedValue("qDotPredictedTempC", color='tab:pink', parseValueFunc=DaveParsFuncs.fluorescenceFuncTemp))

        self.graphs = []
        self.plots = []

        self.plots.append(self.stage1Plot)
        self.plots.append(self.stage1OutputPlot)
        self.plots.append(self.pcrPlot)
        self.plots.append(self.pcrOutputPlot)
        # self.plots.append(self.motorsPlot)
        self.plots.append(errorMsPlot)
        self.plots.append(ratesPlot)
        self.plots.append(self.fluorescencePlot)
        # self.machine_plots = []
        # self.machine_plots.append(self.)
        self.graphs.append(self.plots)
        # self.graphs.append(self.machine_plots)

    def RunPlot(self):
        if self.filename != "":
            timestamps = self.parseLogFile(self.fullPath)
            columns = ["timeSinceBootSeconds"]
            dicts = []

        if len(plt.get_fignums()) >= self.MAXPLOTS:
            for i in plt.get_fignums():
                plt.close(i)
        singlePlot = False
        plotCount = 0
        for plot in self.plots:
            if plot.active:
                plotCount += 1
        if plotCount == 1:
            singlePlot = True
        elif plotCount < 1:
            return
        fig, axs = plt.subplots(plotCount, 1, sharex=True, figsize=(12, 4))

        largestNewYIter = 0
        plotIter = 0
        for plot in self.plots:
            if plot.active:
                if not singlePlot:
                    axs[plotIter].cla()
                pvIter = 0
                newYIter = 0
                for parsedValue in plot.parsedValues:
                    columns.append(parsedValue.name)
                    dicts.append(parsedValue.values)

                    lists = sorted(parsedValue.values.items())
                    if parsedValue.active and len(lists) > 1:
                        if pvIter == 0:
                            NewSubplot(singlePlot, axs, plotIter, parsedValue)
                        else:
                            if parsedValue.mainY:
                                AddToSubplot(singlePlot, axs, plotIter, parsedValue)
                            else:
                                AddToSubplotWithNewY(singlePlot, axs, plotIter, parsedValue, newYIter)
                                newYIter += 1
                    pvIter += 1
                if singlePlot:
                    axs.legend(bbox_to_anchor=(-.09, 1))
                    axs.set_xlabel("Seconds")
                else:
                    axs[plotIter].legend(bbox_to_anchor=(-.09, 1))
                    axs[plotIter].set_xlabel("Seconds")

                if newYIter > largestNewYIter:
                    largestNewYIter = newYIter
                plotIter += 1

        plt.subplots_adjust(right=0.95 - 0.025 * largestNewYIter)
        plt.subplots_adjust(left=0.25)

        if self.parent.auto_write_to_csv_checkbox.isChecked():
            with open(os.path.join(LOCAL_TEST_DATA_FOLDER_NAME, datetime.now().strftime("%Y%m%d_%H%M%S") + ".csv"), 'w',
                      newline='') as ofile:
                writer = csv.writer(ofile, delimiter=',')
                writer.writerow(columns)
                for timestamp in timestamps:
                    row = [timestamp]
                    foundAnyAtTimestamp = False
                    for d in dicts:
                        try:
                            row += [d[timestamp]]
                            foundAnyAtTimestamp = True
                        except:
                            row += ['']
                    if foundAnyAtTimestamp:
                        writer.writerow(row)
            ofile.close()

        plt.show()

    def NewSubplot(self, singlePlot, axs, index, parsedValue):
        if singlePlot:
            obj = axs
        else:
            obj = axs[index]
        lists = sorted(parsedValue.values.items())
        if len(lists) >= 2:
            x, y = zip(*lists)

            if parsedValue.step:
                obj.step(x, y, where='post', color=parsedValue.color, label=parsedValue.name,
                         linewidth=parsedValue.line_width)
            else:
                obj.plot(x, y, color=parsedValue.color, label=parsedValue.name, linewidth=parsedValue.line_width,
                         clip_on=False)
            obj.tick_params(axis='y', labelcolor=parsedValue.color)

    def parseLogFile(self, path):
        previousTimestamp = 0
        timestamps = []
        started = False
        with open(path, 'r') as file:
            line = file.readline()
            while line:
                try:
                    try:

                        # put this back in if data recording start isn't consistent -Van Hoose
                        if not started:
                            if "TC:" in line:
                                started = True
                            else:
                                line = file.readline()
                                continue

                        timestamp = float(line.split("(")[1].split(")")[0])
                        timestamp = timestamp / 1000
                        timestamps.append(timestamp)
                    except:
                        timestamp = previousTimestamp
                    previousTimestamp = timestamp
                    for plot in self.plots:
                        for parsedValue in plot.parsedValues:
                            if parsedValue.parseValueFunc != None:
                                value = parsedValue.parseValueFunc(line)
                                if value != None:
                                    if parsedValue.filterValueFunc != None:
                                        if not parsedValue.filterValueFunc(value):
                                            pass
                                    parsedValue.values[timestamp] = value
                except:
                    pass

                line = file.readline()

        file.close()
        return timestamps

    def run(self):
        pass

        # returns true on sucess. False on error.

    def pickFile(self):
        file_location = QtWidgets.QFileDialog.getOpenFileName(None, "QFileDialog.getSaveFileName()",
                                                              "./" + LOCAL_TEST_DATA_FOLDER_NAME,
                                                              "All Files (*);;Text Files (*.txt)")
        file_location_string = str(file_location[0])

        if file_location_string == "":
            return False

        self.fullPath = file_location_string
        self.filename = os.path.basename(self.fullPath)
        print(self.fullPath)
        return True

    def autoProcessData(self):

        columns = ["timeSinceBootSeconds"]
        dicts = []

        for plot in self.plots:
            for parsedValue in plot.parsedValues:
                columns.append(parsedValue.name)
                dicts.append(parsedValue.values)

        directoryPath = \
            QtWidgets.QFileDialog.getExistingDirectory(None, 'Select Folder Containing Only Viable Log txt Files')
        if directoryPath == "":
            return

        # # pop up progress bar init
        # popup = tk.Toplevel()
        # tk.Label(popup, text="Processing Files").grid(row=0, column=0)
        # progress_var = tk.DoubleVar()
        # progress_bar = Progressbar(popup, variable=progress_var, maximum=100)
        # progress_bar.grid(row=1, column=0, padx=10, pady=5)  # .pack(fill=tk.X, expand=1, side=tk.BOTTOM)
        # popup.pack_slaves()

        # i = 0
        # fileCount = len(os.listdir(directoryPath))
        file = ""
        for file in os.listdir(directoryPath):
            # dicts = []

            # i += 1
            # progress_var.set(i / fileCount * 100)

            # skip files that aren't .txt files
            if file[-3:len(file)] != "txt":
                continue

            fPath = os.path.join(directoryPath, file)

            # check if it is a file
            if os.path.isfile(fPath):
                timestamps = self.parseLogFile(fPath)
                file = file.split('.')[0]
                outfile = file + "RAW" + ".csv"

                if not os.path.exists(AUTO_DAVE_OUTPUT_FOLDER_NAME):
                    os.makedirs(AUTO_DAVE_OUTPUT_FOLDER_NAME)

                with open(os.path.join(AUTO_DAVE_OUTPUT_FOLDER_NAME, outfile), 'w', newline='') as ofile:
                    writer = csv.writer(ofile, delimiter=',')
                    writer.writerow(columns)
                    for timestamp in timestamps:
                        row = [timestamp]
                        foundAnyAtTimestamp = False
                        for d in dicts:
                            try:
                                row += [d[timestamp]]
                                foundAnyAtTimestamp = True
                            except:
                                row += ['']
                        if foundAnyAtTimestamp:
                            writer.writerow(row)
                ofile.close()
                self.daveOutputToPaddedData(os.path.join(os.path.curdir, AUTO_DAVE_OUTPUT_FOLDER_NAME, outfile))

        # popup.destroy()

        sfile = file.split("_")
        sfile = sfile[0:-1]
        newFile = ""
        for seg in sfile:
            newFile += seg + "_"
        newFile = newFile[0:-1]

        self.totalData.to_csv(AUTO_DAVE_OUTPUT_FOLDER_NAME + "/" + newFile + ".csv")
        self.totalData = pd.DataFrame()
        # messagebox.showinfo("AUTO DAVE","Files have been successfully daved")

    def daveOutputToPaddedData(self, fullFilePath):

        df = pd.read_csv(fullFilePath)

        timestamp_Key = 'timeSinceBootSeconds'
        thermistor_temp_key1 = 'Stage1 TempC'
        thermistor_temp_key2 = 'PCR Temp'
        measured_temp_key1 = 'Stage1 Thermocouple TempC'
        measured_temp_key2 = 'PCR Thermocouple TempC'
        modeled_tempC = 'PCR Modeled TempC'
        # TEC_top = 'dataQPcrPeltierTop'
        # TEC_bot = 'dataQPcrPeltierBottom'

        paddedData = df[
            [timestamp_Key, thermistor_temp_key1, thermistor_temp_key2, measured_temp_key1, measured_temp_key2,
             modeled_tempC]]
        # TEC_top, TEC_bot]]

        # if data in file is not the specified type then ignore
        try:
            paddedData = paddedData[
                paddedData[timestamp_Key] > paddedData[timestamp_Key][
                    paddedData[thermistor_temp_key1].first_valid_index()]]
            paddedData = paddedData[
                paddedData[timestamp_Key] < paddedData[timestamp_Key][
                    paddedData[thermistor_temp_key2].last_valid_index()]]
        except:
            try:
                paddedData = paddedData[
                    paddedData[timestamp_Key] > paddedData[timestamp_Key][
                        paddedData[thermistor_temp_key2].first_valid_index()]]
                paddedData = paddedData[
                    paddedData[timestamp_Key] < paddedData[timestamp_Key][
                        paddedData[thermistor_temp_key2].last_valid_index()]]
            except:
                return

        paddedData[timestamp_Key] = (paddedData[timestamp_Key] - paddedData[timestamp_Key].min())

        # trim before first pcrTempC and after last pcrTempC

        dict = {}
        dict[timestamp_Key] = []
        dict[thermistor_temp_key1] = []
        dict[measured_temp_key1] = []
        dict[thermistor_temp_key2] = []
        dict[measured_temp_key2] = []

        dict['padded'] = []

        for i in np.arange(paddedData[timestamp_Key].min(), paddedData[timestamp_Key].max(), 0.05):
            dict[timestamp_Key].append(i)
            dict[thermistor_temp_key1].append(np.NaN)
            dict[measured_temp_key1].append(np.NaN)
            dict[thermistor_temp_key2].append(np.NaN)
            dict[measured_temp_key2].append(np.NaN)
            dict['padded'].append(True)

        paddedData = pd.concat([paddedData, pd.DataFrame.from_dict(dict)], ignore_index=True)
        paddedData.set_index(timestamp_Key, inplace=True)
        paddedData = paddedData.sort_index()
        paddedData[thermistor_temp_key1].interpolate(method='linear', limit_direction='both', inplace=True)
        paddedData[thermistor_temp_key2].interpolate(method='linear', limit_direction='both', inplace=True)
        paddedData[measured_temp_key1].interpolate(method='linear', limit_direction='both', inplace=True)
        paddedData[measured_temp_key2].interpolate(method='linear', limit_direction='both', inplace=True)
        paddedData[modeled_tempC].interpolate(method='linear', limit_direction='both', inplace=True)
        # paddedData[TEC_top].interpolate(method='linear', limit_direction='both', inplace=True)
        # paddedData[TEC_bot].interpolate(method='linear', limit_direction='both', inplace=True)
        paddedData = paddedData[paddedData["padded"].notna()]

        try:
            paddedData = paddedData[
                [thermistor_temp_key1, measured_temp_key1, thermistor_temp_key2, measured_temp_key2]]
        except:
            try:
                paddedData = paddedData[[thermistor_temp_key1, measured_temp_key1]]
            except:
                paddedData = paddedData[[thermistor_temp_key2, measured_temp_key2]]

        fullNameOfFile = os.path.basename(fullFilePath)
        nameOfFile = fullNameOfFile[0:-7] + ".csv"
        paddedData.to_csv(os.path.join(AUTO_DAVE_OUTPUT_FOLDER_NAME, nameOfFile))  # create single files also

        strFile = nameOfFile.split(".csv")[0]
        fileArr = strFile.split("_")

        # one file with all selected checkbox data
        if self.parent.Pcr_checkBox.isChecked() and self.parent.Stg1_checkBox.isChecked():
            groupedData = paddedData[[measured_temp_key1, measured_temp_key2]].copy(deep=True)
            groupedData.rename(
                columns={measured_temp_key1: "stg1_" + fileArr[-1], measured_temp_key2: "pcr_" + fileArr[-1]},
                inplace=True)
        elif self.parent.Stg1_checkBox.isChecked():
            groupedData = paddedData[[measured_temp_key1]].copy(deep=True)
            groupedData.rename(columns={measured_temp_key1: "stg1_" + fileArr[-1]}, inplace=True)
        else:
            groupedData = paddedData[[measured_temp_key2]].copy(deep=True)
            groupedData.rename(columns={measured_temp_key2: "pcr_" + fileArr[-1]}, inplace=True)

        self.totalData = pd.concat([self.totalData, groupedData], axis=1)

        # delete temp raw data files
        for file in os.listdir(AUTO_DAVE_OUTPUT_FOLDER_NAME):
            if "RAW" in file:
                os.remove(os.path.join(AUTO_DAVE_OUTPUT_FOLDER_NAME, file))
