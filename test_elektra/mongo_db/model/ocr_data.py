from mongoengine import *


class OcrFixed(DynamicDocument):
    '''
    Ocr 数据修复，记录所有人工修改OCR的数据。
    
    #FIXME  因要求修改信息必须与就诊人挂勾，所以，此模型当前被废。
    '''
    
    
    meta = {
        "strict": False,
        'indexes': [
            {
                "fields": ["ocr_text","user_id"],
                'name': '_usr_ocr_',
                'unique': True
            }
        ]
    }
    
    user_id = StringField(help_text='谁修改的',required=True)
    create_at = StringField()
    
    ocr_text = StringField(help_text='OCR识别的内容',required=True)
    fix_text = StringField(help_text='修改后的内容',required=True)
    
