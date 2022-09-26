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
        '264313216d6716711e1050ea0f4139781423128',
        '2643120650c0e3f2e8f3fe9fbbd7a5077519292'
        ]

    Runner(l_exercice_id, o_excel_manager, o_api_manager).run()


if __name__ == '__main__':
    main()
