class User:
    """
    Represents osu player as class.
    """

    def __init__(
            self,
            user_id: str,
            username: str,
            count_300: str,
            play_count: str,
            rank: str,
            level: str,
            pp: str,
            total_ss: str,
            total_ssh: str,
            total_s: str,
            total_sh: str,
            country: str,
            accuracy: str,
            country_rank: str,
            profile_image_url: str
    ):
        self._user_id = user_id
        self._username = username
        self._count_300 = count_300
        self._play_count = play_count
        self._rank = rank
        self._level = level
        self._pp = pp
        self._total_ss = total_ss
        self._total_ssh = total_ssh
        self._total_s = total_s
        self._total_sh = total_sh
        self._country = country
        self._accuracy = accuracy
        self._country_rank = country_rank
        self._profile_image_url = profile_image_url

    @property
    def user_id(self) -> int:
        try:
            return int(self._user_id)
        except ValueError:
            return 0

    @property
    def username(self) -> str:
        return self._username

    @property
    def accuracy(self) -> float:
        return round(float(self._accuracy))

    @property
    def count_300(self) -> int:
        try:
            return int(self._count_300)
        except ValueError:
            return 0

    @property
    def play_count(self) -> int:
        try:
            return int(self._play_count)
        except ValueError:
            return 0

    @property
    def rank(self) -> int:
        try:
            return int(self._rank)
        except ValueError:
            return 0

    @property
    def country_rank(self) -> int:
        try:
            return int(self._country_rank)
        except ValueError:
            return 0

    @property
    def level(self) -> int:
        try:
            return int(round(float(self._level)))
        except ValueError:
            return 0

    @property
    def pp(self) -> int:
        try:
            return int(round(float(self._pp)))
        except ValueError:
            return 0

    @property
    def total_ss(self) -> int:
        try:
            return int(self._total_ss) + int(self._total_ssh)
        except ValueError:
            return 0

    @property
    def total_s(self) -> int:
        try:
            return int(self._total_s) + int(self._total_sh)
        except ValueError:
            return 0

    @property
    def country(self) -> str:
        return self._country

    @property
    def profile_image_url(self) -> str:
        return self._profile_image_url
