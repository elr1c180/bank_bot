import aiohttp


ROOT_URL = 'http://217.196.98.13:9000/'

async def create_user(chat_id, username, first_name):
    user_data = {"chat_id": chat_id, "username": username, "name": first_name}
    async with aiohttp.ClientSession() as session:
        async with session.post(ROOT_URL + 'create_user/', data=user_data) as resp:
            return {await resp.text(), resp.status}