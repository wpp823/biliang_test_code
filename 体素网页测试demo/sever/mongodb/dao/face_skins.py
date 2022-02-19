from mongodb.model.face_skin_analysis_result import FaceBoxObj, ColorObj, SkinTypeObj, CategoryObj, SensitiveObj, ProblemObj, WrinkleObj, WrinkleCarteObj, \
    RoughnessObj, InflammationObj, InflammationDxObj, ProblemBubblesObj, AcneObj, SkinTestDataResult
from utils.skinanalysis import FaceSkinItem


class FaceSkinsDao():
    def __init__(self, log):
        self.log = log
        self.collection = 'skin_test_result'

    def add(self, face_skin_data: FaceSkinItem):
        """

        @return:
        """
        res = None
        try:
            skin_post_data = SkinTestDataResult(
                request_id=face_skin_data.request_id,
                version=face_skin_data.version,
                skin_age=face_skin_data.skin_age,
                original_image=face_skin_data.original_image,
                face_crop=face_skin_data.face_crop,
                overall_score=face_skin_data.overall_score,

                face_box=FaceBoxObj(**face_skin_data.face_box),
                color=ColorObj(**face_skin_data.color),
                skin_type=SkinTypeObj(
                    score=face_skin_data.skin_type.get("score", 0),
                    category=[CategoryObj(**item) for item in face_skin_data.skin_type.get("category", [])],
                    type=face_skin_data.skin_type.get("type", ''),
                    wiki=face_skin_data.skin_type.get("wiki", ''),
                    tips=face_skin_data.skin_type.get("tips", ''),
                    # document_type = ""
                ),
                sensitive=SensitiveObj(**face_skin_data.sensitive),
                dark_circle=ProblemObj(**face_skin_data.dark_circle),
                pore=ProblemObj(**face_skin_data.pore),
                wrinkle=WrinkleObj(
                    problem_score=face_skin_data.wrinkle.get("problem_score", None),
                    tips=face_skin_data.wrinkle.get("tips", ""),
                    wiki=face_skin_data.wrinkle.get("wiki", ""),
                    filename=face_skin_data.wrinkle.get("filename", ""),
                    category=[WrinkleCarteObj(**item) for item in face_skin_data.wrinkle.get("category", [])],
                ),
                blackhead=ProblemObj(**face_skin_data.blackhead),
                roughness=RoughnessObj(**face_skin_data.roughness),
                hyperpigmentations=InflammationObj(
                    problem_score=face_skin_data.hyperpigmentations.get("problem_score", None),
                    dx_list=[InflammationDxObj(**item) for item in face_skin_data.hyperpigmentations.get("dx_list", [])]
                ),
                problem_bubbles=[ProblemBubblesObj(**item) for item in face_skin_data.problem_bubbles],
                acne=AcneObj(
                    problem_score=face_skin_data.acne.get("problem_score"),
                    tips=face_skin_data.acne.get("problem_score"),
                    wiki=face_skin_data.acne.get("problem_score"),
                    filename=face_skin_data.acne.get("problem_score"),
                    category=[WrinkleCarteObj(**item) for item in face_skin_data.acne.get("category", [])],
                    stage=face_skin_data.acne.get("problem_score"),
                ),
                inflammations=InflammationObj(
                    problem_score=face_skin_data.inflammations.get("problem_score", None),
                    dx_list=[InflammationDxObj(**item) for item in face_skin_data.inflammations.get("dx_list", [])]
                )
            )

            res = skin_post_data.save()
        except:
            self.log.exception("[FaceSkinsDao.add][face_skin_data:{}]".format(face_skin_data))

        return res

    def update(self, face_skin_data: FaceSkinItem):
        """
        更新测肤结果

        @param face_skin_data:
        @return:
        """
