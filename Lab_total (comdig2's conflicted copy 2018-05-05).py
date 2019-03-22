#!/usr/bin/env python2
# -*- coding: utf-8 -*-
##################################################
# GNU Radio Python Flow Graph
# Title: Lab Total
# Generated: Fri May  4 15:17:13 2018
##################################################

if __name__ == '__main__':
    import ctypes
    import sys
    if sys.platform.startswith('linux'):
        try:
            x11 = ctypes.cdll.LoadLibrary('libX11.so')
            x11.XInitThreads()
        except:
            print "Warning: failed to XInitThreads()"

import os
import sys
sys.path.append(os.environ.get('GRC_HIER_PATH', os.path.expanduser('~/.grc_gnuradio')))

from PyQt4 import Qt
from b_M_PAM_bb import b_M_PAM_bb  # grc-generated hier_block
from b_PCM_Encoder_Bb import b_PCM_Encoder_Bb  # grc-generated hier_block
from b_RRaised_cosine_cc import b_RRaised_cosine_cc  # grc-generated hier_block
from gnuradio import blocks
from gnuradio import digital
from gnuradio import eng_notation
from gnuradio import gr
from gnuradio import uhd
from gnuradio.eng_option import eng_option
from gnuradio.filter import firdes
from gnuradio.qtgui import Range, RangeWidget
from optparse import OptionParser
from scipy import fftpack
import cmath
import math
import numpy
import random
import time


class Lab_total(gr.top_block, Qt.QWidget):

    def __init__(self):
        gr.top_block.__init__(self, "Lab Total")
        Qt.QWidget.__init__(self)
        self.setWindowTitle("Lab Total")
        try:
            self.setWindowIcon(Qt.QIcon.fromTheme('gnuradio-grc'))
        except:
            pass
        self.top_scroll_layout = Qt.QVBoxLayout()
        self.setLayout(self.top_scroll_layout)
        self.top_scroll = Qt.QScrollArea()
        self.top_scroll.setFrameStyle(Qt.QFrame.NoFrame)
        self.top_scroll_layout.addWidget(self.top_scroll)
        self.top_scroll.setWidgetResizable(True)
        self.top_widget = Qt.QWidget()
        self.top_scroll.setWidget(self.top_widget)
        self.top_layout = Qt.QVBoxLayout(self.top_widget)
        self.top_grid_layout = Qt.QGridLayout()
        self.top_layout.addLayout(self.top_grid_layout)

        self.settings = Qt.QSettings("GNU Radio", "Lab_total")
        self.restoreGeometry(self.settings.value("geometry").toByteArray())

        ##################################################
        # Variables
        ##################################################
        self.samp_rate_usrp_rx = samp_rate_usrp_rx = 100e6
        self.Kd = Kd = 512
        self.samp_rate = samp_rate = int(samp_rate_usrp_rx/Kd)
        self.Sps = Sps = 4
        self.Constelacion = Constelacion = [(1+0j), (0+1j), (-1+0j), (0 -1j)]
        self.Rs = Rs = samp_rate/Sps
        self.M = M = len(Constelacion)
        self.rolloff = rolloff = 0.9
        self.code1 = code1 = '010110011011101100010101011111101001001110001011010001101010001'
        self.W = W = Rs/2.
        self.Bps = Bps = int(math.log(M,2))
        self.payload = payload = 128
        self.ntaps = ntaps = Sps*16
        self.nfilts = nfilts = 32
        self.Rb = Rb = Rs*Bps
        self.NbpCode = NbpCode = len(code1)+10.
        self.BW = BW = W*(1.+rolloff)
        self.run_stop = run_stop = True
        self.rrc_taps_rx = rrc_taps_rx = firdes.root_raised_cosine(nfilts, nfilts, 1.0/float(Sps), rolloff, ntaps*nfilts)
        self.eq_gain = eq_gain = 0.01
        self.Tmax_scope = Tmax_scope = 64./Rs
        self.Sps_o = Sps_o = 4
        self.Rbi = Rbi = Rb/(1+NbpCode/payload)
        self.MiconstellationObject = MiconstellationObject = digital.constellation_calcdist((Constelacion), (), 4, 1).base()
        self.Gain_USRP_Tx_dB = Gain_USRP_Tx_dB = 30.
        self.Gain_USRP_Rx_dB = Gain_USRP_Rx_dB = 20
        self.Fc = Fc = 900e6
        self.B_usrp = B_usrp = samp_rate
        self.B = B = 2*BW

        ##################################################
        # Blocks
        ##################################################
        self.controls = Qt.QTabWidget()
        self.controls_widget_0 = Qt.QWidget()
        self.controls_layout_0 = Qt.QBoxLayout(Qt.QBoxLayout.TopToBottom, self.controls_widget_0)
        self.controls_grid_layout_0 = Qt.QGridLayout()
        self.controls_layout_0.addLayout(self.controls_grid_layout_0)
        self.controls.addTab(self.controls_widget_0, "Tuning")
        self.top_grid_layout.addWidget(self.controls, 0,1,1,1)
        self.Instrumentos = Qt.QTabWidget()
        self.Instrumentos_widget_0 = Qt.QWidget()
        self.Instrumentos_layout_0 = Qt.QBoxLayout(Qt.QBoxLayout.TopToBottom, self.Instrumentos_widget_0)
        self.Instrumentos_grid_layout_0 = Qt.QGridLayout()
        self.Instrumentos_layout_0.addLayout(self.Instrumentos_grid_layout_0)
        self.Instrumentos.addTab(self.Instrumentos_widget_0, "Capa0.Canal y precanal")
        self.Instrumentos_widget_1 = Qt.QWidget()
        self.Instrumentos_layout_1 = Qt.QBoxLayout(Qt.QBoxLayout.TopToBottom, self.Instrumentos_widget_1)
        self.Instrumentos_grid_layout_1 = Qt.QGridLayout()
        self.Instrumentos_layout_1.addLayout(self.Instrumentos_grid_layout_1)
        self.Instrumentos.addTab(self.Instrumentos_widget_1, "Capas.Pre-modulacion")
        self.Instrumentos_widget_2 = Qt.QWidget()
        self.Instrumentos_layout_2 = Qt.QBoxLayout(Qt.QBoxLayout.TopToBottom, self.Instrumentos_widget_2)
        self.Instrumentos_grid_layout_2 = Qt.QGridLayout()
        self.Instrumentos_layout_2.addLayout(self.Instrumentos_grid_layout_2)
        self.Instrumentos.addTab(self.Instrumentos_widget_2, "Capa1. Modulacion")
        self.Instrumentos_widget_3 = Qt.QWidget()
        self.Instrumentos_layout_3 = Qt.QBoxLayout(Qt.QBoxLayout.TopToBottom, self.Instrumentos_widget_3)
        self.Instrumentos_grid_layout_3 = Qt.QGridLayout()
        self.Instrumentos_layout_3.addLayout(self.Instrumentos_grid_layout_3)
        self.Instrumentos.addTab(self.Instrumentos_widget_3, "Capa2. CodificacionDeSimbolos")
        self.top_grid_layout.addWidget(self.Instrumentos, 1,0,1,2)
        self._Gain_USRP_Tx_dB_range = Range(0., 130, 1, 30., 200)
        self._Gain_USRP_Tx_dB_win = RangeWidget(self._Gain_USRP_Tx_dB_range, self.set_Gain_USRP_Tx_dB, "Gain_USRP_Tx (dB)", "counter", float)
        self.controls_grid_layout_0.addWidget(self._Gain_USRP_Tx_dB_win, 0,1,1,1)
        self.uhd_usrp_sink_0 = uhd.usrp_sink(
        	",".join(("", "")),
        	uhd.stream_args(
        		cpu_format="fc32",
        		channels=range(1),
        	),
        )
        self.uhd_usrp_sink_0.set_samp_rate(samp_rate)
        self.uhd_usrp_sink_0.set_center_freq(Fc, 0)
        self.uhd_usrp_sink_0.set_gain(Gain_USRP_Tx_dB, 0)
        self.uhd_usrp_sink_0.set_antenna("TX/RX", 0)
        _run_stop_check_box = Qt.QCheckBox("Inicial/Parar")
        self._run_stop_choices = {True: True, False: False}
        self._run_stop_choices_inv = dict((v,k) for k,v in self._run_stop_choices.iteritems())
        self._run_stop_callback = lambda i: Qt.QMetaObject.invokeMethod(_run_stop_check_box, "setChecked", Qt.Q_ARG("bool", self._run_stop_choices_inv[i]))
        self._run_stop_callback(self.run_stop)
        _run_stop_check_box.stateChanged.connect(lambda i: self.set_run_stop(self._run_stop_choices[bool(i)]))
        self.top_grid_layout.addWidget(_run_stop_check_box, 0,0,1,1)
        self.digital_diff_encoder_bb_0 = digital.diff_encoder_bb(M)
        self.digital_chunks_to_symbols_xx_0 = digital.chunks_to_symbols_bc((Constelacion), 1)
        self.canal = Qt.QTabWidget()
        self.canal_widget_0 = Qt.QWidget()
        self.canal_layout_0 = Qt.QBoxLayout(Qt.QBoxLayout.TopToBottom, self.canal_widget_0)
        self.canal_grid_layout_0 = Qt.QGridLayout()
        self.canal_layout_0.addLayout(self.canal_grid_layout_0)
        self.canal.addTab(self.canal_widget_0, "Constelacion")
        self.canal_widget_1 = Qt.QWidget()
        self.canal_layout_1 = Qt.QBoxLayout(Qt.QBoxLayout.TopToBottom, self.canal_widget_1)
        self.canal_grid_layout_1 = Qt.QGridLayout()
        self.canal_layout_1.addLayout(self.canal_grid_layout_1)
        self.canal.addTab(self.canal_widget_1, "Espectro")
        self.canal_widget_2 = Qt.QWidget()
        self.canal_layout_2 = Qt.QBoxLayout(Qt.QBoxLayout.TopToBottom, self.canal_widget_2)
        self.canal_grid_layout_2 = Qt.QGridLayout()
        self.canal_layout_2.addLayout(self.canal_grid_layout_2)
        self.canal.addTab(self.canal_widget_2, "Medidores")
        self.canal_widget_3 = Qt.QWidget()
        self.canal_layout_3 = Qt.QBoxLayout(Qt.QBoxLayout.TopToBottom, self.canal_widget_3)
        self.canal_grid_layout_3 = Qt.QGridLayout()
        self.canal_layout_3.addLayout(self.canal_grid_layout_3)
        self.canal.addTab(self.canal_widget_3, "histograma")
        self.Instrumentos_grid_layout_0.addWidget(self.canal, 1,0,1,1)
        self.blocks_file_source_0 = blocks.file_source(gr.sizeof_char*1, "/home/comdig2/Dropbox/_comdiguis/Lab.FaseII/Lab2.5/texto2.txt", True)
        self.b_RRaised_cosine_cc_0 = b_RRaised_cosine_cc(
            Ganancia=1.,
            Interpolation=Sps,
            ntaps=ntaps*Sps,
            rolloff=rolloff,
            sps=Sps,
        )
        self.b_PCM_Encoder_Bb_0 = b_PCM_Encoder_Bb(
            code=code1,
            payload=payload,
        )
        self.b_M_PAM_bb_0 = b_M_PAM_bb(
            M=M,
            Nbps=8,
        )
        self.Pre_modulacion = Qt.QTabWidget()
        self.Pre_modulacion_widget_0 = Qt.QWidget()
        self.Pre_modulacion_layout_0 = Qt.QBoxLayout(Qt.QBoxLayout.TopToBottom, self.Pre_modulacion_widget_0)
        self.Pre_modulacion_grid_layout_0 = Qt.QGridLayout()
        self.Pre_modulacion_layout_0.addLayout(self.Pre_modulacion_grid_layout_0)
        self.Pre_modulacion.addTab(self.Pre_modulacion_widget_0, "Capa8.Mensaje continuo")
        self.Pre_modulacion_widget_1 = Qt.QWidget()
        self.Pre_modulacion_layout_1 = Qt.QBoxLayout(Qt.QBoxLayout.TopToBottom, self.Pre_modulacion_widget_1)
        self.Pre_modulacion_grid_layout_1 = Qt.QGridLayout()
        self.Pre_modulacion_layout_1.addLayout(self.Pre_modulacion_grid_layout_1)
        self.Pre_modulacion.addTab(self.Pre_modulacion_widget_1, "Capa7.Cuantificacion")
        self.Pre_modulacion_widget_2 = Qt.QWidget()
        self.Pre_modulacion_layout_2 = Qt.QBoxLayout(Qt.QBoxLayout.TopToBottom, self.Pre_modulacion_widget_2)
        self.Pre_modulacion_grid_layout_2 = Qt.QGridLayout()
        self.Pre_modulacion_layout_2.addLayout(self.Pre_modulacion_grid_layout_2)
        self.Pre_modulacion.addTab(self.Pre_modulacion_widget_2, "Capa6.PCM")
        self.Pre_modulacion_widget_3 = Qt.QWidget()
        self.Pre_modulacion_layout_3 = Qt.QBoxLayout(Qt.QBoxLayout.TopToBottom, self.Pre_modulacion_widget_3)
        self.Pre_modulacion_grid_layout_3 = Qt.QGridLayout()
        self.Pre_modulacion_layout_3.addLayout(self.Pre_modulacion_grid_layout_3)
        self.Pre_modulacion.addTab(self.Pre_modulacion_widget_3, "Capa5.Otrastecnicas")
        self.Pre_modulacion_widget_4 = Qt.QWidget()
        self.Pre_modulacion_layout_4 = Qt.QBoxLayout(Qt.QBoxLayout.TopToBottom, self.Pre_modulacion_widget_4)
        self.Pre_modulacion_grid_layout_4 = Qt.QGridLayout()
        self.Pre_modulacion_layout_4.addLayout(self.Pre_modulacion_grid_layout_4)
        self.Pre_modulacion.addTab(self.Pre_modulacion_widget_4, "Capa4.CodificacionBinaria")
        self.Pre_modulacion_widget_5 = Qt.QWidget()
        self.Pre_modulacion_layout_5 = Qt.QBoxLayout(Qt.QBoxLayout.TopToBottom, self.Pre_modulacion_widget_5)
        self.Pre_modulacion_grid_layout_5 = Qt.QGridLayout()
        self.Pre_modulacion_layout_5.addLayout(self.Pre_modulacion_grid_layout_5)
        self.Pre_modulacion.addTab(self.Pre_modulacion_widget_5, "Capa3.M-PAM")
        self.Instrumentos_grid_layout_1.addWidget(self.Pre_modulacion, 1,0,1,1)
        self._Gain_USRP_Rx_dB_range = Range(0., 130, 1, 20, 200)
        self._Gain_USRP_Rx_dB_win = RangeWidget(self._Gain_USRP_Rx_dB_range, self.set_Gain_USRP_Rx_dB, "Gain_USRP_Rx (dB)", "counter", float)
        self.controls_grid_layout_0.addWidget(self._Gain_USRP_Rx_dB_win, 0,2,1,1)

        ##################################################
        # Connections
        ##################################################
        self.connect((self.b_M_PAM_bb_0, 0), (self.digital_diff_encoder_bb_0, 0))    
        self.connect((self.b_PCM_Encoder_Bb_0, 0), (self.b_M_PAM_bb_0, 0))    
        self.connect((self.b_RRaised_cosine_cc_0, 0), (self.uhd_usrp_sink_0, 0))    
        self.connect((self.blocks_file_source_0, 0), (self.b_PCM_Encoder_Bb_0, 0))    
        self.connect((self.digital_chunks_to_symbols_xx_0, 0), (self.b_RRaised_cosine_cc_0, 0))    
        self.connect((self.digital_diff_encoder_bb_0, 0), (self.digital_chunks_to_symbols_xx_0, 0))    

    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "Lab_total")
        self.settings.setValue("geometry", self.saveGeometry())
        event.accept()


    def get_samp_rate_usrp_rx(self):
        return self.samp_rate_usrp_rx

    def set_samp_rate_usrp_rx(self, samp_rate_usrp_rx):
        self.samp_rate_usrp_rx = samp_rate_usrp_rx
        self.set_samp_rate(int(self.samp_rate_usrp_rx/self.Kd))

    def get_Kd(self):
        return self.Kd

    def set_Kd(self, Kd):
        self.Kd = Kd
        self.set_samp_rate(int(self.samp_rate_usrp_rx/self.Kd))

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.set_B_usrp(self.samp_rate)
        self.set_Rs(self.samp_rate/self.Sps)
        self.uhd_usrp_sink_0.set_samp_rate(self.samp_rate)

    def get_Sps(self):
        return self.Sps

    def set_Sps(self, Sps):
        self.Sps = Sps
        self.set_Rs(self.samp_rate/self.Sps)
        self.set_ntaps(self.Sps*16)
        self.set_rrc_taps_rx(firdes.root_raised_cosine(self.nfilts, self.nfilts, 1.0/float(self.Sps), self.rolloff, self.ntaps*self.nfilts))
        self.b_RRaised_cosine_cc_0.set_Interpolation(self.Sps)
        self.b_RRaised_cosine_cc_0.set_ntaps(self.ntaps*self.Sps)
        self.b_RRaised_cosine_cc_0.set_sps(self.Sps)

    def get_Constelacion(self):
        return self.Constelacion

    def set_Constelacion(self, Constelacion):
        self.Constelacion = Constelacion
        self.set_M(len(self.Constelacion))
        self.digital_chunks_to_symbols_xx_0.set_symbol_table((self.Constelacion))

    def get_Rs(self):
        return self.Rs

    def set_Rs(self, Rs):
        self.Rs = Rs
        self.set_Rb(self.Rs*self.Bps)
        self.set_Tmax_scope(64./self.Rs)
        self.set_W(self.Rs/2.)

    def get_M(self):
        return self.M

    def set_M(self, M):
        self.M = M
        self.set_Bps(int(math.log(self.M,2)))
        self.b_M_PAM_bb_0.set_M(self.M)

    def get_rolloff(self):
        return self.rolloff

    def set_rolloff(self, rolloff):
        self.rolloff = rolloff
        self.set_BW(self.W*(1.+self.rolloff))
        self.set_rrc_taps_rx(firdes.root_raised_cosine(self.nfilts, self.nfilts, 1.0/float(self.Sps), self.rolloff, self.ntaps*self.nfilts))
        self.b_RRaised_cosine_cc_0.set_rolloff(self.rolloff)

    def get_code1(self):
        return self.code1

    def set_code1(self, code1):
        self.code1 = code1
        self.set_NbpCode(len(self.code1)+10.)
        self.b_PCM_Encoder_Bb_0.set_code(self.code1)

    def get_W(self):
        return self.W

    def set_W(self, W):
        self.W = W
        self.set_BW(self.W*(1.+self.rolloff))

    def get_Bps(self):
        return self.Bps

    def set_Bps(self, Bps):
        self.Bps = Bps
        self.set_Rb(self.Rs*self.Bps)

    def get_payload(self):
        return self.payload

    def set_payload(self, payload):
        self.payload = payload
        self.set_Rbi(self.Rb/(1+self.NbpCode/self.payload))
        self.b_PCM_Encoder_Bb_0.set_payload(self.payload)

    def get_ntaps(self):
        return self.ntaps

    def set_ntaps(self, ntaps):
        self.ntaps = ntaps
        self.set_rrc_taps_rx(firdes.root_raised_cosine(self.nfilts, self.nfilts, 1.0/float(self.Sps), self.rolloff, self.ntaps*self.nfilts))
        self.b_RRaised_cosine_cc_0.set_ntaps(self.ntaps*self.Sps)

    def get_nfilts(self):
        return self.nfilts

    def set_nfilts(self, nfilts):
        self.nfilts = nfilts
        self.set_rrc_taps_rx(firdes.root_raised_cosine(self.nfilts, self.nfilts, 1.0/float(self.Sps), self.rolloff, self.ntaps*self.nfilts))

    def get_Rb(self):
        return self.Rb

    def set_Rb(self, Rb):
        self.Rb = Rb
        self.set_Rbi(self.Rb/(1+self.NbpCode/self.payload))

    def get_NbpCode(self):
        return self.NbpCode

    def set_NbpCode(self, NbpCode):
        self.NbpCode = NbpCode
        self.set_Rbi(self.Rb/(1+self.NbpCode/self.payload))

    def get_BW(self):
        return self.BW

    def set_BW(self, BW):
        self.BW = BW
        self.set_B(2*self.BW)

    def get_run_stop(self):
        return self.run_stop

    def set_run_stop(self, run_stop):
        self.run_stop = run_stop
        if self.run_stop: self.start()
        else: self.stop(); self.wait()
        self._run_stop_callback(self.run_stop)

    def get_rrc_taps_rx(self):
        return self.rrc_taps_rx

    def set_rrc_taps_rx(self, rrc_taps_rx):
        self.rrc_taps_rx = rrc_taps_rx

    def get_eq_gain(self):
        return self.eq_gain

    def set_eq_gain(self, eq_gain):
        self.eq_gain = eq_gain

    def get_Tmax_scope(self):
        return self.Tmax_scope

    def set_Tmax_scope(self, Tmax_scope):
        self.Tmax_scope = Tmax_scope

    def get_Sps_o(self):
        return self.Sps_o

    def set_Sps_o(self, Sps_o):
        self.Sps_o = Sps_o

    def get_Rbi(self):
        return self.Rbi

    def set_Rbi(self, Rbi):
        self.Rbi = Rbi

    def get_MiconstellationObject(self):
        return self.MiconstellationObject

    def set_MiconstellationObject(self, MiconstellationObject):
        self.MiconstellationObject = MiconstellationObject

    def get_Gain_USRP_Tx_dB(self):
        return self.Gain_USRP_Tx_dB

    def set_Gain_USRP_Tx_dB(self, Gain_USRP_Tx_dB):
        self.Gain_USRP_Tx_dB = Gain_USRP_Tx_dB
        self.uhd_usrp_sink_0.set_gain(self.Gain_USRP_Tx_dB, 0)
        	

    def get_Gain_USRP_Rx_dB(self):
        return self.Gain_USRP_Rx_dB

    def set_Gain_USRP_Rx_dB(self, Gain_USRP_Rx_dB):
        self.Gain_USRP_Rx_dB = Gain_USRP_Rx_dB

    def get_Fc(self):
        return self.Fc

    def set_Fc(self, Fc):
        self.Fc = Fc
        self.uhd_usrp_sink_0.set_center_freq(self.Fc, 0)

    def get_B_usrp(self):
        return self.B_usrp

    def set_B_usrp(self, B_usrp):
        self.B_usrp = B_usrp

    def get_B(self):
        return self.B

    def set_B(self, B):
        self.B = B


def main(top_block_cls=Lab_total, options=None):

    from distutils.version import StrictVersion
    if StrictVersion(Qt.qVersion()) >= StrictVersion("4.5.0"):
        style = gr.prefs().get_string('qtgui', 'style', 'raster')
        Qt.QApplication.setGraphicsSystem(style)
    qapp = Qt.QApplication(sys.argv)

    tb = top_block_cls()
    tb.start()
    tb.show()

    def quitting():
        tb.stop()
        tb.wait()
    qapp.connect(qapp, Qt.SIGNAL("aboutToQuit()"), quitting)
    qapp.exec_()


if __name__ == '__main__':
    main()
