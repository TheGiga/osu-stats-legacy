from .errors import UserNotFound
from .osu import get, User


class Api:
    def __init__(
            self,
            api_key: str
    ):
        """
        :type api_key: String-like api key
        """
        self._api_key = api_key
        self._api_endpoint = "https://osu.ppy.sh/api"

    async def get_osu_player(self, name: str, mode: str = 'osu!') -> User:
        """
        :type name: Player's name
        :type mode: osu! game mode e.g osu!, osu!mania etc

        :rtype: osu.User
        """
        params = {
            'k': self._api_key,
            'u': name,
            'm': mode,
            'type': 'string'
        }
        data = await get(f'{self._api_endpoint}/get_user', params=params)

        try:
            obj = User(
                user_id=data[0].get('user_id'),
                username=data[0].get('username'),
                count_300=data[0].get('count300'),
                play_count=data[0].get('playcount'),
                rank=data[0].get('pp_rank'),
                country_rank=data[0].get('pp_country_rank'),
                level=data[0].get('level'),
                pp=data[0].get('pp_raw'),
                total_ss=data[0].get('count_rank_ss'),
                total_ssh=data[0].get('count_rank_ssh'),
                total_s=data[0].get('count_rank_s'),
                total_sh=data[0].get('count_rank_sh'),
                country=data[0].get('country'),
                accuracy=data[0].get('accuracy'),
                profile_image_url=f'http://s.ppy.sh/a/{data[0].get("user_id")}'
            )
        except IndexError:
            raise UserNotFound

        return obj
