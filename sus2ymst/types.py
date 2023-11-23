from dataclasses import dataclass


class TapType:
    Normal = 1
    Critical = 2


# タップノーツ
@dataclass
class TapNote:
    tick: int
    lane: int
    width: int
    type: int  # 1: 通常ノーツ, 2: クリティカルノーツ


class FlickDirectionType:
    Up = 1
    Left = 3
    Right = 4


# フリックノーツ
@dataclass
class FlickNote:
    tick: int
    lane: int
    width: int
    direction: int  # 1: 上, 3: 左, 4: 右


# スクラッチノーツ
@dataclass
class ScratchNote:
    tick: int
    lane: int
    width: int


class HoldType:
    Normal = 0
    Critical = 1
    Scratch = 2
    ScratchCritical = 3
    Start = 4


# ホールドノーツ
@dataclass
class HoldNote:
    tick: int
    end_tick: int
    lane: int
    width: int
    type: int  # HoldType
    gimmick_type: int
    movement: int
    scratch_start: bool


@dataclass
class HoldScratchNote:
    tick: int
    lane: int
    width: int
    movement: int


@dataclass
class SoundNote:
    tick: int
    lane: int
    width: int
    type: int


@dataclass
class HoldEighthNote:
    tick: int
    lane: int
    width: int


@dataclass
class SplitNote:
    tick: int
    end_tick: int
    lane: int
    gimmick_type: int
    id: int


class NoteType:
    None_ = 0
    Normal = 10
    Critical = 20
    Sound = 30
    SoundPurple = 31
    Scratch = 40
    Flick = 50
    HoldStart = 80
    CriticalHoldStart = 81
    ScratchHoldStart = 82
    ScratchCriticalHoldStart = 83
    Hold = 100
    CriticalHold = 101
    ScratchHold = 110
    ScratchCriticalHold = 111
    HoldEighth = 900


class GimmickType:
    None_ = 0
    JumpScratch = 1
    OneDirection = 2
    Split1 = 11
    Split2 = 12
    Split3 = 13
    Split4 = 14
    Split5 = 15
    Split6 = 16


SplitIds = [
    1,
    2,
    3,
    4,
    5,
    6,
    7,
    8,
    9,
    1010,
    1020,
    1030,
    1040,
    1050,
    1060,
    2010,
    2020,
    2030,
    2040,
    2050,
    3010,
    3020,
    3030,
    3040,
    3050,
    4010,
    4020,
    4030,
    4040,
    4050,
    10010,
    10020,
    10030,
    10040,
    10050,
    10060,
    10070,
    10080,
    10100,
    10110,
    10120,
    10130,
    10140,
    10150,
    10160,
    10161,
    10162,
    10170,
    10180,
    10190,
    10191,
    10192,
    10200,
    10210,
    10230,
    10240,
    10250,
    10260,
    10320,
    10321,
    10322,
    10323,
    10324,
    10325,
    10326,
    10327,
    10328,
    10340,
    10350,
    10360,
    10361,
    10390,
    10391,
    10392,
    10393,
]
