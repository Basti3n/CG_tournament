from dataclasses import dataclass, field
from typing import List, Dict

from xlsxwriter import Workbook


@dataclass
class ExcelManager:
    s_game_name: str
    s_folder_path: str = field(init=False, default='resources')
    o_workbook: Workbook = field(init=False)

    def __post_init__(self):
        self.o_workbook = Workbook(f'{self.s_folder_path}/CG_tournament_{self.s_game_name}.xlsx')

    def create_score_sheet(self, dc_players: Dict[str, int]) -> None:
        o_worksheet = self.o_workbook.add_worksheet('Score')
        data = [[s_player_name, i_score] for i, (s_player_name, i_score) in enumerate(dc_players.items())]
        self._write_header(o_worksheet, data, 'Score')

    @staticmethod
    def _write_header(o_worksheet, l_score: List[List[str | int]], s_exercise_id: str) -> None:
        o_worksheet.set_column(0, 1, 25)
        o_worksheet.add_table(f'A1:B{len(l_score) + 1}',
                              {'data': l_score,
                               'autofilter': False,
                               'name': f'marklist_{s_exercise_id}',
                               'columns': [
                                   {'header': 'Player Name'},
                                   {'header': 'Total Points'}
                               ]
                               })

    def close(self):
        self.o_workbook.close()

    def write_results_beautify(self, s_exercise_id: str, l_results: List[str]):
        o_worksheet = self.o_workbook.add_worksheet(s_exercise_id[:31])
        o_worksheet.set_column(0, 1, 25)
        data = [[s_result, len(l_results) - i] for i, s_result in enumerate(l_results)]
        self._write_header(o_worksheet, data, s_exercise_id)

