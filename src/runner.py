import logging
from dataclasses import dataclass
from typing import List, Dict

from src.api_manager import ApiManager
from src.excel_manager import ExcelManager

o_logger = logging.getLogger(__name__)


@dataclass
class Runner:
    l_exercise_ids: List[str]
    o_excel_manager: ExcelManager
    o_api_manager: ApiManager

    def run(self):
        dc_players = {}
        for s_exercise_id in self.l_exercise_ids:
            l_exercise_result = self.o_api_manager.get_results(s_exercise_id)

            dc_players_scores = self._calcul_points(l_exercise_result)
            for s_player_name, i_score in dc_players_scores.items():
                dc_players[s_player_name] = dc_players.get(s_player_name, 0) + i_score

            self.o_excel_manager.write_results_beautify(s_exercise_id, l_exercise_result)
        dc_played_ordered = dict(sorted(dc_players.items(), key=lambda item: item[1], reverse=True))
        self.o_excel_manager.create_score_sheet(dc_played_ordered)

        self.o_excel_manager.close()

    @staticmethod
    def _calcul_points(l_exercise_result) -> Dict[str, int]:
        return {s_player_name: len(l_exercise_result) - i_score for i_score, s_player_name in
                enumerate(l_exercise_result)}
