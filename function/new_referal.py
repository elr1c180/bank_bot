import aiohttp


ROOT_URL = 'http://217.196.98.13:9000/'

async def new_ref(chat_id, username, first_name, link_owner):
    user_data = {"referal": chat_id, "username": username, "name": first_name, 'link_owner':link_owner}
    async with aiohttp.ClientSession() as session:
        async with session.post(ROOT_URL + 'new-ref/', data=user_data) as resp:
            return {await resp.text(), resp.status}