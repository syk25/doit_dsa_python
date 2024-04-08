from enum import Enum
from chained_hash import ChainedHash

Menu = Enum('Menu', ['추가','삭제','검색','덤프','종료'])

def select_menu() -> Menu:
    """메뉴 선택"""
    S = []