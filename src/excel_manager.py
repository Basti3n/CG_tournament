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

    def write_results(self, s_exercise_id: str, l_results: List[str]):
        o_worksheet = self.o_workbook.add_worksheet(s_exercise_id[:31])

        s_column_a = 'Player Name'
        s_column_b = 'Points'
        o_worksheet.write(f'A1', s_column_a)
        o_worksheet.write(f'B1', s_column_b)

        for i, s_result in enumerate(l_results):
            o_worksheet.write(f'A{i + 2}', s_result)
            o_worksheet.write(f'B{i + 2}', i)

    def create_score_sheet(self, dc_players: Dict[str, int]) -> None:
        o_worksheet = self.o_workbook.add_worksheet("Score")
        s_column_a = 'Player Name'
        s_column_b = 'Total Points'
        o_worksheet.write(f'A1', s_column_a)
        o_worksheet.write(f'B1', s_column_b)
        for i,(s_player_name, i_score) in enumerate(dc_players.items()):
            o_worksheet.write(f'A{i + 2}', s_player_name)
            o_worksheet.write(f'B{i + 2}', i_score)

    def close(self):
        self.o_workbook.close()
