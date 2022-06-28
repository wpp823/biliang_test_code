from tornado import web, ioloop


class IndexHandler(web.RequestHandler):
    def get(self):
        data = {
            "order_ids": [
                1111, 111122, 1223123123, 12312312
            ]
        }
        return self.render("nightcrawler_wx_order_user.html", data_items=data)


settings = {
    "handlers": [
        ('/', IndexHandler)
    ],
    "debug": True,
    "template_path": './'
}

app = web.Application(
    **settings
)
app.listen(port=8283)

ioloop.IOLoop.instance().start()
