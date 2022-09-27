import logging

from src.api_manager import ApiManager
from src.excel_manager import ExcelManager
from src.logger_configuration import setup_logging_configuration
from src.runner import Runner

o_logger = logging.getLogger(__name__)


def main() -> None:
    s_script_name = 'CG_tournament'
    s_tournament_name = 'Fridays'
    setup_logging_configuration('INFO', s_script_name)

    o_logger.info('Start of the script')

    o_excel_manager = ExcelManager(s_tournament_name)
    o_api_manager = ApiManager()
    l_exercice_id = [
        '26454410a0198904f51696d4f7e14875a3b88a4',
        '264541859d1c3d801283bea370d738a6fbd9f24',
        '2645399faf1c1d6fd67e95971170879516d18bd',
        '2645388938bbb5f98127be27c10426e5d55260c'
        ]

    Runner(l_exercice_id, o_excel_manager, o_api_manager).run()


if __name__ == '__main__':
    main()
