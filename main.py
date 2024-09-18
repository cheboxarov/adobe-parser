import asyncio
import aiohttp
from openpyxl import load_workbook
from bs4 import BeautifulSoup
from adobe import AsyncClient


async def main():
    wb = load_workbook('test.xlsx')
    ws = wb.active

    tasks = []

    empty_cells = 0

    for row in ws.iter_rows():
        url = row[0].value
        name = row[1].value

        if name is None:
            empty_cells += 1
            tasks.append(fill_asset_name(url, row))

    if empty_cells == 0:
        print("Нет пустых ячеек имен")
        return
    print(f"Обрабатываю {empty_cells} страниц")
    await asyncio.gather(*tasks)

    wb.save('test.xlsx')
    print("Изменения сохранены в test.xlsx")


async def fill_asset_name(url, row):
    try:
        adobe_client = AsyncClient()
        asset_name = await adobe_client.get_asset_name(url)
        row[1].value = asset_name
    except:
        row[1].value = "Error!"


if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(main())
