import pymongo

# 本地
# MONGO_HOST_PART = "mongodb://root:@192.168.1.230"
# 测试服
MONGO_HOST_PART = ""
# 正式服
# MONGO_HOST_PART = ""
MONGO_HOST_AUTH_DB = "admin"
MONGO_HOST_REPLICA_SET = None

MONGO_HOST = MONGO_HOST_PART + "/" + MONGO_HOST_AUTH_DB

MONGO_DB_NAME = 'daredevil'


class Tools:
    def __init__(self):
        self.conn = pymongo.MongoClient(MONGO_HOST)
        self.db = self.conn["daredevil"]

    def update_voice_content(self):
        query_con = {"type": 34}

        wx_messages = self.db["wx_message"]
        data = wx_messages.find(query_con)
        for item in data:
            content = item.get('content')
            voice_len = int(content.split(":")[1])
            msg_id = item.get('msg_id')
            update_data = {
                "$set": {
                    "msg_type": "voice",
                    "msg_content": {
                        'url': '',
                        "upload_id": "",
                        'length': voice_len,
                        "text": ""
                    }
                }
            }
            con_data = {"msg_id": msg_id}
            wx_messages.update_one(con_data, update_data)
            print("update_wx_messages,msg_id:{}".format(msg_id))

        print("end")


if __name__ == "__main__":
    tools = Tools()
    tools.update_voice_content()
