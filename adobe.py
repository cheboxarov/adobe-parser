import requests
from bs4 import BeautifulSoup
import aiohttp


class Client:

    def __init__(self):
        self.session = requests.Session()
        self.session.headers = {
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
            'accept-language': 'ru,en;q=0.9',
            'cache-control': 'max-age=0',
            # 'cookie': 'Variant_flex=1; AdobeStock=16b762d23df36e636f0eeae358a800d5; asui=dcbcf657401d5e93b4056b93db802ed0; isid=2cb06e5e0f344fb30839c726ea334f6e596897ea; ffuuid=UNbuhWpZOi7VGKU1qWX3Cw%3D%3D; gabt=78873790900000%3A0%2C1680740330%3A0%2C8789744682%3A0%2Cchecksum; mboxDisable=true; isVisitorScriptAloneHosted=1; s_ecid=MCMID%7C75096245378321815863327575388715152690; AMCVS_9E1005A551ED61CA0A490D45%40AdobeOrg=1; last_selected_asset_type=all; OptanonAlertBoxClosed=2024-09-18T09:28:30.590Z; OptanonConsent=groups=C0001%3A1%2CC0002%3A1%2CC0003%3A1%2CC0004%3A1; OptanonChoice=1; Variant_flex=1; _gcl_au=1.1.1205171104.1726651711; _fbp=fb.1.1726651711592.377479669227833544; _pin_unauth=dWlkPU1ETmlOVEUyWXpjdFpHUmlPUzAwWlRoakxUa3lZekF0TUdKa016TXpPRFkxT0dWaw; AMCV_9E1005A551ED61CA0A490D45%40AdobeOrg=1585540135%7CMCIDTS%7C19985%7CMCMID%7C75096245378321815863327575388715152690%7CMCAID%7CNONE%7CMCOPTOUT-1726658913s%7CNONE%7CMCAAMLH-1727256513%7C6%7CMCAAMB-1727256513%7Cj8Odv6LonN4r3an7LhD3WZrU1bUpAkFkkiY1ncBR96t2PTI%7CMCSYNCSOP%7C411-19992%7CMCCIDH%7C-1411949976%7CvVersion%7C4.4.0; s_cc=true; kndctr_9E1005A551ED61CA0A490D45_AdobeOrg_cluster=irl1; kndctr_9E1005A551ED61CA0A490D45_AdobeOrg_identity=CiY3NTA5NjI0NTM3ODMyMTgxNTg2MzMyNzU3NTM4ODcxNTE1MjY5MFIRCIPf2aOgMhgBKgRJUkwxMAPwAYPf2aOgMg==; s_ppv=[%22stock.adobe.com/es/images/top-view-of-outd%22%2C100%2C0%2C1032%2C1920%2C1032%2C1920%2C1080%2C1%2C%22P%22]; visp=assetDetailPg%3A1726652400; maxmind_country=NL; s_nr=1726652318944-New; _uetsid=5e9923d075a011efac44d3f8411534db; _uetvid=5e994c6075a011ef9b9457e695bc3c1f; gpv=stock.adobe.com:images:retro-chandelier-on-transparent-background:868123604',
            'dnt': '1',
            'priority': 'u=0, i',
            'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'document',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-site': 'same-origin',
            'sec-fetch-user': '?1',
            'upgrade-insecure-requests': '1',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36',
        }

        cookies = {
            'Variant_flex': '1',
            'AdobeStock': '16b762d23df36e636f0eeae358a800d5',
            'asui': 'dcbcf657401d5e93b4056b93db802ed0',
            'isid': '2cb06e5e0f344fb30839c726ea334f6e596897ea',
            'ffuuid': 'UNbuhWpZOi7VGKU1qWX3Cw%3D%3D',
            'gabt': '78873790900000%3A0%2C1680740330%3A0%2C8789744682%3A0%2Cchecksum',
            'mboxDisable': 'true',
            'isVisitorScriptAloneHosted': '1',
            's_ecid': 'MCMID%7C75096245378321815863327575388715152690',
            'AMCVS_9E1005A551ED61CA0A490D45%40AdobeOrg': '1',
            'last_selected_asset_type': 'all',
            'OptanonAlertBoxClosed': '2024-09-18T09:28:30.590Z',
            'OptanonConsent': 'groups=C0001%3A1%2CC0002%3A1%2CC0003%3A1%2CC0004%3A1',
            'OptanonChoice': '1',
            'Variant_flex': '1',
            '_gcl_au': '1.1.1205171104.1726651711',
            '_fbp': 'fb.1.1726651711592.377479669227833544',
            '_pin_unauth': 'dWlkPU1ETmlOVEUyWXpjdFpHUmlPUzAwWlRoakxUa3lZekF0TUdKa016TXpPRFkxT0dWaw',
            'AMCV_9E1005A551ED61CA0A490D45%40AdobeOrg': '1585540135%7CMCIDTS%7C19985%7CMCMID%7C75096245378321815863327575388715152690%7CMCAID%7CNONE%7CMCOPTOUT-1726658913s%7CNONE%7CMCAAMLH-1727256513%7C6%7CMCAAMB-1727256513%7Cj8Odv6LonN4r3an7LhD3WZrU1bUpAkFkkiY1ncBR96t2PTI%7CMCSYNCSOP%7C411-19992%7CMCCIDH%7C-1411949976%7CvVersion%7C4.4.0',
            's_cc': 'true',
            'kndctr_9E1005A551ED61CA0A490D45_AdobeOrg_cluster': 'irl1',
            'kndctr_9E1005A551ED61CA0A490D45_AdobeOrg_identity': 'CiY3NTA5NjI0NTM3ODMyMTgxNTg2MzMyNzU3NTM4ODcxNTE1MjY5MFIRCIPf2aOgMhgBKgRJUkwxMAPwAYPf2aOgMg==',
            's_ppv': '[%22stock.adobe.com/es/images/top-view-of-outd%22%2C100%2C0%2C1032%2C1920%2C1032%2C1920%2C1080%2C1%2C%22P%22]',
            'visp': 'assetDetailPg%3A1726652400',
            'maxmind_country': 'NL',
            's_nr': '1726652318944-New',
            '_uetsid': '5e9923d075a011efac44d3f8411534db',
            '_uetvid': '5e994c6075a011ef9b9457e695bc3c1f',
            'gpv': 'stock.adobe.com:images:retro-chandelier-on-transparent-background:868123604',
        }

        for key, value in cookies.items():
            self.session.cookies.set(key, value)

    def get_asset_name(self, url: str):
        asset_id = url.split("/")[-1]
        if "?" in asset_id:
            asset_id = asset_id.split("?")[0]
        params = {
            'asset_id': asset_id,
        }

        response = self.session.get(url, params=params)
        soup = BeautifulSoup(response.text, 'html.parser')
        title = soup.find("meta", itemprop="name").get("content")
        return title


class AsyncClient:

    def __init__(self):
        self.cookies={
            'Variant_flex': '1',
            'AdobeStock': '16b762d23df36e636f0eeae358a800d5',
            'asui': 'dcbcf657401d5e93b4056b93db802ed0',
            'isid': '2cb06e5e0f344fb30839c726ea334f6e596897ea',
            'ffuuid': 'UNbuhWpZOi7VGKU1qWX3Cw%3D%3D',
            'gabt': '78873790900000%3A0%2C1680740330%3A0%2C8789744682%3A0%2Cchecksum',
            'mboxDisable': 'true',
            'isVisitorScriptAloneHosted': '1',
            's_ecid': 'MCMID%7C75096245378321815863327575388715152690',
            'AMCVS_9E1005A551ED61CA0A490D45%40AdobeOrg': '1',
            'last_selected_asset_type': 'all',
            'OptanonAlertBoxClosed': '2024-09-18T09:28:30.590Z',
            'OptanonConsent': 'groups=C0001%3A1%2CC0002%3A1%2CC0003%3A1%2CC0004%3A1',
            'OptanonChoice': '1',
            'Variant_flex': '1',
            '_gcl_au': '1.1.1205171104.1726651711',
            '_fbp': 'fb.1.1726651711592.377479669227833544',
            '_pin_unauth': 'dWlkPU1ETmlOVEUyWXpjdFpHUmlPUzAwWlRoakxUa3lZekF0TUdKa016TXpPRFkxT0dWaw',
            'AMCV_9E1005A551ED61CA0A490D45%40AdobeOrg': '1585540135%7CMCIDTS%7C19985%7CMCMID%7C75096245378321815863327575388715152690%7CMCAID%7CNONE%7CMCOPTOUT-1726658913s%7CNONE%7CMCAAMLH-1727256513%7C6%7CMCAAMB-1727256513%7Cj8Odv6LonN4r3an7LhD3WZrU1bUpAkFkkiY1ncBR96t2PTI%7CMCSYNCSOP%7C411-19992%7CMCCIDH%7C-1411949976%7CvVersion%7C4.4.0',
            's_cc': 'true',
            'kndctr_9E1005A551ED61CA0A490D45_AdobeOrg_cluster': 'irl1',
            'kndctr_9E1005A551ED61CA0A490D45_AdobeOrg_identity': 'CiY3NTA5NjI0NTM3ODMyMTgxNTg2MzMyNzU3NTM4ODcxNTE1MjY5MFIRCIPf2aOgMhgBKgRJUkwxMAPwAYPf2aOgMg==',
            's_ppv': '[%22stock.adobe.com/es/images/top-view-of-outd%22%2C100%2C0%2C1032%2C1920%2C1032%2C1920%2C1080%2C1%2C%22P%22]',
            'visp': 'assetDetailPg%3A1726652400',
            'maxmind_country': 'NL',
            's_nr': '1726652318944-New',
            '_uetsid': '5e9923d075a011efac44d3f8411534db',
            '_uetvid': '5e994c6075a011ef9b9457e695bc3c1f',
            'gpv': 'stock.adobe.com:images:retro-chandelier-on-transparent-background:868123604',
        }
        self.headers={
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
            'accept-language': 'ru,en;q=0.9',
            'cache-control': 'max-age=0',
            # 'cookie': 'Variant_flex=1; AdobeStock=16b762d23df36e636f0eeae358a800d5; asui=dcbcf657401d5e93b4056b93db802ed0; isid=2cb06e5e0f344fb30839c726ea334f6e596897ea; ffuuid=UNbuhWpZOi7VGKU1qWX3Cw%3D%3D; gabt=78873790900000%3A0%2C1680740330%3A0%2C8789744682%3A0%2Cchecksum; mboxDisable=true; isVisitorScriptAloneHosted=1; s_ecid=MCMID%7C75096245378321815863327575388715152690; AMCVS_9E1005A551ED61CA0A490D45%40AdobeOrg=1; last_selected_asset_type=all; OptanonAlertBoxClosed=2024-09-18T09:28:30.590Z; OptanonConsent=groups=C0001%3A1%2CC0002%3A1%2CC0003%3A1%2CC0004%3A1; OptanonChoice=1; Variant_flex=1; _gcl_au=1.1.1205171104.1726651711; _fbp=fb.1.1726651711592.377479669227833544; _pin_unauth=dWlkPU1ETmlOVEUyWXpjdFpHUmlPUzAwWlRoakxUa3lZekF0TUdKa016TXpPRFkxT0dWaw; AMCV_9E1005A551ED61CA0A490D45%40AdobeOrg=1585540135%7CMCIDTS%7C19985%7CMCMID%7C75096245378321815863327575388715152690%7CMCAID%7CNONE%7CMCOPTOUT-1726658913s%7CNONE%7CMCAAMLH-1727256513%7C6%7CMCAAMB-1727256513%7Cj8Odv6LonN4r3an7LhD3WZrU1bUpAkFkkiY1ncBR96t2PTI%7CMCSYNCSOP%7C411-19992%7CMCCIDH%7C-1411949976%7CvVersion%7C4.4.0; s_cc=true; kndctr_9E1005A551ED61CA0A490D45_AdobeOrg_cluster=irl1; kndctr_9E1005A551ED61CA0A490D45_AdobeOrg_identity=CiY3NTA5NjI0NTM3ODMyMTgxNTg2MzMyNzU3NTM4ODcxNTE1MjY5MFIRCIPf2aOgMhgBKgRJUkwxMAPwAYPf2aOgMg==; s_ppv=[%22stock.adobe.com/es/images/top-view-of-outd%22%2C100%2C0%2C1032%2C1920%2C1032%2C1920%2C1080%2C1%2C%22P%22]; visp=assetDetailPg%3A1726652400; maxmind_country=NL; s_nr=1726652318944-New; _uetsid=5e9923d075a011efac44d3f8411534db; _uetvid=5e994c6075a011ef9b9457e695bc3c1f; gpv=stock.adobe.com:images:retro-chandelier-on-transparent-background:868123604',
            'dnt': '1',
            'priority': 'u=0, i',
            'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'document',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-site': 'same-origin',
            'sec-fetch-user': '?1',
            'upgrade-insecure-requests': '1',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36',
        }

    async def get_asset_name(self, url: str) -> str:
        async with aiohttp.ClientSession(headers=self.headers, cookies=self.cookies) as session:
            asset_id = url.split('/')[-1]
            if "?" in asset_id:
                asset_id = asset_id.split("?")[0]
            params = {"asset_id": asset_id}

            async with session.get(url, params=params) as response:
                response_text = await response.text()
                soup = BeautifulSoup(response_text, 'html.parser')
                title = soup.find("meta", itemprop="name").get("content")
                return title
