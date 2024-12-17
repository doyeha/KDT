from PyQt5.QtCore import pyqtSignal, QObject


class signal_collection(QObject):
    go_Mainview_signal = pyqtSignal(bool)
    idpw_signal = pyqtSignal(str, str, bool)    # ID, PW, login_try
    open_driver_Mainview_signal = pyqtSignal(bool)
    reset_idpw_signal = pyqtSignal(bool)
    login_success_signal = pyqtSignal(bool)
    start_crawling_signal = pyqtSignal(str, str, bool, bool, bool, bool, int)

    # 크롤링 쓰레드에서 - 저장쓰레드로 저장할 데이터 전달
    link_saver_signal = pyqtSignal(str, str)
    # data_saver_signal = pyqtSignal(str, str, str, str,str)
    data_saver_signal = pyqtSignal(tuple)

    # con 연결 닫는 용.
    closecon_signal = pyqtSignal(bool)


    link_crawl_end_signal = pyqtSignal(int)

    crawl_links_send_signal = pyqtSignal(list)

    link_inset_while_signal = pyqtSignal(bool)
    data_inset_while_signal = pyqtSignal(bool)

    # 링크가 모두 큐를 통해 저장되었는지에 대한 정보 전송 시그널
    link_save_complete_signal = pyqtSignal(bool)
    load_data_signal = pyqtSignal(tuple)


    # labeler로 setText 신호 보내는 ~ 시스템 시그널
    system_message_signal = pyqtSignal(str)

    # 세부사항 전달
    mini_condition_signal = pyqtSignal(int, int)

    

    def __init__(self):
        super().__init__()

