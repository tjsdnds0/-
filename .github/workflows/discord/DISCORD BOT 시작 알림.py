author = await client.get_user("Your ID").create_dm()
        await author.send("on_ready가 호출되었습니다.")
