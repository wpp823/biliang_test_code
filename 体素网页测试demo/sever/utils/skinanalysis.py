from utils.vocel_cloud_api import VocelCloudApi


class FaceSkinItem(dict):

    @property
    def request_id(self):
        return self.get("request_id", None)

    @property
    def version(self):
        return self.get("version", None)

    @property
    def skin_age(self):
        return self.get("skin_age", None)

    @property
    def original_image(self):
        return self.get("original_image", None)

    @property
    def face_crop(self):
        return self.get("face_crop", None)

    @property
    def overall_score(self):
        return self.get("overall_score", None)

    @property
    def face_box(self):
        return self.get("face_box", {})

    @property
    def color(self):
        return self.get("color", {})

    @property
    def skin_type(self):
        return self.get("skin_type", {})

    @property
    def sensitive(self):
        return self.get("sensitive", {})

    @property
    def dark_circle(self):
        return self.get("dark_circle", {})

    @property
    def pore(self):
        return self.get("pore", {})

    @property
    def wrinkle(self):
        return self.get("wrinkle", {})

    @property
    def blackhead(self):
        return self.get("blackhead", {})

    @property
    def roughness(self):
        return self.get("roughness", {})

    @property
    def hyperpigmentations(self):
        return self.get("hyperpigmentations", {})

    @property
    def problem_bubbles(self):
        return self.get("problem_bubbles", {})

    @property
    def acne(self):
        return self.get("acne", {})

    @property
    def inflammations(self):
        return self.get("inflammations", {})


class SkinAnalysis(VocelCloudApi):

    def post_img_url(self, img_url):
        """
        通过图片url地址请求数据

        @return:
        """

        url = "/derms/v1/skinanalysis"
        media_type = "Image_URL"
        data = {
            "access_key": self.access_key,
            "secret_key": self.secret_key,
            "media_data": img_url,
            "media_type": media_type
        }
        ret_data = None
        try:
            response = self._post(url=url, data=data)
            if response:
                code = response.get("code")
                if code == 200:
                    self._log.info("[SkinAnalysis.post_img_url_ok][url:{},data:{}][response:{}]".format(img_url, data, response))
                    res_data = response.get("data")
                    ret_data = FaceSkinItem(*res_data)
                else:
                    self._log.error("[SkinAnalysis.post_img_url_ok][url:{},data:{}][response:{}]".format(img_url, data, response))
        except:
            self._log.exception("[SkinAnalysis.post_img_url_ok][url:{},data:{}]".format(img_url, data))
        return ret_data

    def post_base64_img(self, img_base64):
        """
        通过图片base64获取结果

        @param img_base64:
        @return:
        """
        url = "/derms/v1/skinanalysis"
        media_type = "Image_Base64_String"

        data = {
            "access_key": self.access_key,
            "secret_key": self.secret_key,
            "media_data": img_base64,
            "media_type": media_type
        }
        ret_data = None
        try:
            response = self._post(url=url, data=data)
            if response:
                code = response.get("code")
                if code == 200:
                    self._log.info("[SkinAnalysis.post_base64_img_ok][img_base64:{},data:{}][response:{}]".format(img_base64, data, response))
                    res_data = response.get("data")
                    ret_data = FaceSkinItem(*res_data)
                else:
                    self._log.error("[SkinAnalysis.post_base64_img_ok][img_base64:{},data:{}][response:{}]".format(img_base64, data, response))
        except:
            self._log.exception("[SkinAnalysis.post_base64_img_ok][img_base64:{},data:{}]".format(img_base64, data))
        return ret_data
