

### 面部要求
    完整头部照片，半身照，证件照无法找到脸部
    返回数据格式：部分节点无，也可能未检测到相关问题

### 数据字段说明





![](../../../man.jpg)

#### 男性大头照返回数据
```    {
        "request_id" : "MTY0NDQ2MzgzMS43MDIzNzM=",
        "version" : "derms-v1.2.1",
        "skin_age" : NumberInt(31),
        "original_image" : "https://wechat-skin-v1-prod.oss-cn-shanghai.aliyuncs.com/results%2F2022-02-10%2FMTY0NDQ2MzgzMS43MDIzNzM%3D%2Forigin_image.jpg?OSSAccessKeyId=LTAI4G8HUwXM84nxSgadaVLP&Expires=1644464134&Signature=iSZ2vEfmt5cJLPOpXyThJKhaJ5o%3D",
        "face_crop" : "https://wechat-skin-v1-prod.oss-cn-shanghai.aliyuncs.com/results%2F2022-02-10%2FMTY0NDQ2MzgzMS43MDIzNzM%3D%2Fface_crop.jpg?x-oss-process=image%2Fresize%2Cm_fill%2Ch_240%2Cw_240%2Climit_0&OSSAccessKeyId=LTAI4G8HUwXM84nxSgadaVLP&Expires=1644464134&Signature=eHGFy4Y%2BROakyuXZ66meawpU1e8%3D",
        "overall_score" : NumberInt(91),
        "face_box" : {
            "x0" : NumberInt(174),
            "y0" : NumberInt(132),
            "x1" : NumberInt(589),
            "y1" : NumberInt(711)
        },
        "color" : {
            "result" : "baixi",
            "wiki" : "人的肤色主要由两个因素决定：皮肤内各种色素的含量；表皮的厚度和光线在皮肤表面的散射情况。只有从这两个因素着手，才可以让皮肤呈现白皙、细腻、完美无瑕的肤色。皮肤血液循环状态、皮肤表面光线反射、不良生活习惯及精神神经因素都会影响皮肤颜色。“白里透红”是亚洲人理想和健康的皮肤颜色。",
            "tips" : "你拥有较为白皙的肤色。穿衣搭配对大多数风格都能hold住，真令人羡慕呢。不过肤色越白意味着皮肤黑色素含量越低。黑色素的主要作用是吸收紫外线，因此你对紫外线抵抗能力较弱，平时一定要注意做好防晒，保持充足的睡眠，适度的运动。"
        },
        "skin_type" : {
            "score" : NumberInt(62),
            "category" : [
                {
                    "cls" : "forehead",
                    "type" : "mid",
                    "score" : NumberInt(65)
                },
                {
                    "cls" : "nose",
                    "type" : "oil",
                    "score" : NumberInt(66)
                },
                {
                    "cls" : "left_cheek",
                    "type" : "oil",
                    "score" : NumberInt(70)
                },
                {
                    "cls" : "right_cheek",
                    "type" : "mid",
                    "score" : NumberInt(48)
                },
                {
                    "cls" : "chin",
                    "type" : "oil",
                    "score" : NumberInt(66)
                }
            ],
            "type" : "oil",
            "wiki" : "干性、中性和油性皮肤的分法，主要来自于皮脂分泌量的区别。\n中性皮肤：皮脂分泌量正常，皮肤角质层水含量正常（10-20%），皮肤紧致，有弹性，表面光滑润泽，细腻，是最理想的皮肤状态，一般只有婴幼儿和青少年才能拥有该类肤质。\n干性皮肤：皮脂分泌量低，皮肤角质层水含量低（<10%）,皮肤干燥脱屑，细腻但无光泽，肤色晦暗，易出现细小皱纹，色素沉着。\n油性皮肤：皮脂分泌量大，皮肤角质层含水量正常或者偏低，皮肤表面油腻，有光泽，毛孔粗大，易发生痤疮、毛囊炎。\n中性肌肤：皮肤皮脂腺和汗腺分泌较平衡，皮肤可以形成健康的皮脂末角质层保存适量的水分。但皮肤容易受到季节、环境、身体状况的影响而发生变化。\n混合性肌肤：在脸部的不同部位出现干性和油性的双重特征，皮肤虽也会出现夏季偏油、冬季偏干的状况，但T字区(前额、鼻翼和下巴)偏油，两颊偏干。",
            "tips" : "你属于中性偏油的皮肤。平时用35°的温水清洁，使用产品的清洁力略高，每2周可以做一次去角质。选用收敛控油的化妆水，选择带有控油功能的保湿乳液或者啫喱，尽量选择防晒乳液（防晒霜过于厚重），适当使用防晒喷雾，结合稍微控油的保湿，是你这类肤质的工作重点。"
        },
        "sensitive" : {
            "score" : NumberInt(1),
            "type" : "tolerance",
            "tips" : "无敏感情况，皮肤屏障功能良好，对寒冷、炎热、化妆品、酒精或药物等外界刺激无反应。平时合理清洁、适度保湿、加强防晒、保持合理水分即可。",
            "wiki" : "敏感性肌肤的特征\n1.皮肤表皮薄，皮脂分泌少，较干燥，微血管明显，皮肤呈现干燥机能减退，角质层保持水分的能力降低，肌肤表面的皮脂膜形成不完全。  \n2.接触化妆品或季节过敏后易引起皮肤过敏，出现红、肿、 痒。皮肤缺乏光泽，脸颊易充血红肿。  \n3.因季节变化而使皮肤容易呈现不稳定的状态。主要症状是搔痒、烧灼感、刺痛、皮肤发痒和出小疹子。  \n4.容易受冷风、食物、水质、紫外线、合成纤维、香味等外在环境或物质的影响。  \n5.单接触到刺激性物质就会引发肌肤的问题。对阳光、气候、水、植物（花粉）、化妆品、香水、蚊虫叮咬及高蛋白食物都有可能导致过敏。 "
        },
        "dark_circle" : {
            "_cls" : "ProblemObj",
            "problem_score" : NumberInt(66),
            "tips" : "你有混合型黑眼圈，平时可以通过在眼睛周围涂抹维生素E、K1和视黄醇混合物或者热敷来改善眼部血液循环。平时还要注意防晒，出门戴太阳镜、涂防晒霜，使用柔和的眼部化妆品，及时卸妆等来预防。还有注意不要熬夜、不要过度用眼，保证足够的睡眠，平时仰睡和不要用力揉眼都有利于缓解混合型黑眼圈。",
            "wiki" : "黑眼圈有三种：色素型，血管型、阴影型。\n色素型黑眼圈：日晒、眼周皮肤病、皮肤损伤、化妆品沉积等黑色素过度沉积引起眼圈周围颜色加深。\n血管型黑眼圈：眼睛周围的皮肤很薄，如果局部血液循环不好，血液中去氧的血红蛋白增多，血管通过眼睑皮肤透出青紫色，造成颜色黯淡。\n阴影型黑眼圈：眼睛周围的皮肤下垂、肌肉松弛、导致眼袋突出，造成局部阴影，让人看起来好像有很重的黑眼圈，其实是眼睛周围的结构发生变化，形成阴影，造成黑眼圈。",
            "type" : "HHX"
        },
        "pore" : {
            "_cls" : "ProblemObj",
            "problem_score" : NumberInt(0),
            "tips" : "没有毛孔粗大的情况。以预防为主，平时坚持运动（如跑步、快走一类的有氧运动），减少糖分及牛奶的摄入，减少熬夜，保持规律作息，降低工作压力，饮食均衡即可。",
            "wiki" : "毛孔粗大的原因来自于皮脂分泌旺盛，多余的油脂不能及时清除，进而堵塞毛孔，使毛孔膨胀，造成皮肤弹性松弛，最后毛囊粗大。此外，慢性复发性痤疮、性激素、抽烟喝酒、睡眠不足和不当皮肤护理都可影响毛孔大小。"
        },
        "wrinkle" : {
            "_cls" : "WrinkleObj",
            "problem_score" : NumberInt(15),
            "tips" : "你有轻微的眼下细纹，表现为皮纹加深，刚可辨认，似折痕虚。如因水份不足引起，请使用滋润眼霜轻轻按摩；如因眼过度引起，请不要过度使用眼睛，要经常放松，眺望远方；如因血液循环不佳引起，可以多运动，或者用发热眼罩等热敷。",
            "wiki" : "皱纹的形成：皮肤的正常衰老、皮肤附属器官功能的自然衰退、皮肤的新陈代谢减慢，使得真皮层的弹性纤维和胶原纤维逐渐老化，使皮肤的张力和弹力减弱；丰富的面部表情；长期的睡眠不足、皮肤缺水、不当的减肥、缺乏体育锻炼；化妆品的使用不当、烟酒的刺激。\n皱纹分为真性皱纹和假性皱纹。真性皱纹是面部形成的非手术或注射不能祛除的稳定性皱纹，此种皮肤的胶原纤维和弹力纤维性能下降，导致皮肤失去韧性和弹性；假性皱纹是面部出现的不稳定性的皱纹，是由于皮肤暂时性的缺水或缺乏油脂滋润引起的，这类皱纹可以通过皮肤弹性的自我调节或通过皮肤护理在一定时间内自行消退。\n\n",
            "filename" : "https://wechat-skin-v1-prod.oss-cn-shanghai.aliyuncs.com/results%2F2022-02-10%2FMTY0NDQ2MzgzMS43MDIzNzM%3D%2Fwrinkle_image.jpg?OSSAccessKeyId=LTAI4G8HUwXM84nxSgadaVLP&Expires=1644464135&Signature=Z50SmAgbRe8YMDygGvJZBw448E4%3D",
            "category" : [
                {
                    "cls" : "forehead",
                    "problem_score" : NumberInt(0),
                    "level" : "none"
                },
                {
                    "cls" : "eyecorner",
                    "problem_score" : NumberInt(10),
                    "level" : "lightly"
                },
                {
                    "cls" : "crowfeet",
                    "problem_score" : NumberInt(0),
                    "level" : "none"
                },
                {
                    "cls" : "glabella",
                    "problem_score" : NumberInt(0),
                    "level" : "none"
                },
                {
                    "cls" : "nasolabial",
                    "problem_score" : NumberInt(84),
                    "level" : "lightly"
                }
            ]
        },
        "blackhead" : {
            "_cls" : "ProblemObj",
            "problem_score" : NumberInt(0),
            "tips" : "没有黑头，以预防为主。 少吃糖，少喝含糖饮料，比如奶茶，可乐；少吃盐，不要吃盐含量太高的食物；减轻自身压力，增加运动，调节工作节奏。",
            "wiki" : "黑头称开放性粉刺 ，主要是由皮脂、细胞屑和细菌组成的一种“栓”样物，阻塞在毛囊开口处而形成的，加上空气中的尘埃、污垢和氧化作用，使其接触空气的一头逐渐变黑，经氧化后成为黑色的小点，这些小点就是被称作黑头的油脂阻塞物。"
        },
        "roughness" : {
            "problem_score" : NumberInt(5),
            "tips" : "你的皮肤非常光滑，请继续保持哟。",
            "wiki" : "影响皮肤表面状态的粗燥与平滑度的因素很多，常见的有皮肤水分油分、斑点、纹理（皱纹）等。皮肤表面纹理细小、表浅，且走向柔和是青春美丽的皮肤外观。但随着年龄的增加和环境因素的影响，皮肤纹理会逐渐增大、增粗，皱纹形成并逐渐加深。"
        },
        "hyperpigmentations" : {
            "dx_list" : [ ]
        },
        "problem_bubbles" : [
            {          
                "name" : "dark_circle",
                "score" : NumberInt(66)
            },
            {
                "name" : "wrinkle",
                "score" : NumberInt(15)
            },
            {
                "name" : "roughness",
                "score" : NumberInt(5)
            },
            {
                "name" : "pore",
                "score" : NumberInt(0)
            },
            {
                "name" : "blackhead",
                "score" : NumberInt(0)
            }
        ],
        "acne" : {
            "category" : [ ]
        },
        "inflammations" : {
            "dx_list" : [ ]
        }
    }
```
![](/Users/wyy/Desktop/woman.jpg)

#### 女性大头照返回数据

```{
	"_id" : ObjectId("6204b8e28676152b6dcd2add"),
	"request_id" : "MTY0NDQ3NjYzNi43NzU3NzU0",
	"version" : "derms-v1.2.1",
	"skin_age" : NumberInt(29),
	"original_image" : "https://wechat-skin-v1-prod.oss-cn-shanghai.aliyuncs.com/results%2F2022-02-10%2FMTY0NDQ3NjYzNi43NzU3NzU0%2Forigin_image.jpg?OSSAccessKeyId=LTAI4G8HUwXM84nxSgadaVLP&Expires=1644476941&Signature=LWwiAQe7UZFoNzB3EMMWVUk2WaY%3D",
	"face_crop" : "https://wechat-skin-v1-prod.oss-cn-shanghai.aliyuncs.com/results%2F2022-02-10%2FMTY0NDQ3NjYzNi43NzU3NzU0%2Fface_crop.jpg?x-oss-process=image%2Fresize%2Cm_fill%2Ch_240%2Cw_240%2Climit_0&OSSAccessKeyId=LTAI4G8HUwXM84nxSgadaVLP&Expires=1644476941&Signature=T6z6YwGQYFHg%2Bx98DoAyLa0763s%3D",
	"overall_score" : NumberInt(78),
	"face_box" : {
		"x0" : NumberInt(116),
		"y0" : NumberInt(108),
		"x1" : NumberInt(594),
		"y1" : NumberInt(783)
	},
	"color" : {
		"result" : "baixi",
		"wiki" : "人的肤色主要由两个因素决定：皮肤内各种色素的含量；表皮的厚度和光线在皮肤表面的散射情况。只有从这两个因素着手，才可以让皮肤呈现白皙、细腻、完美无瑕的肤色。皮肤血液循环状态、皮肤表面光线反射、不良生活习惯及精神神经因素都会影响皮肤颜色。“白里透红”是亚洲人理想和健康的皮肤颜色。",
		"tips" : "你拥有较为白皙的肤色。穿衣搭配对大多数风格都能hold住，真令人羡慕呢。不过肤色越白意味着皮肤黑色素含量越低。黑色素的主要作用是吸收紫外线，因此你对紫外线抵抗能力较弱，平时一定要注意做好防晒，保持充足的睡眠，适度的运动。"
	},
	"skin_type" : {
		"score" : NumberInt(59),
		"category" : [
			{
				"cls" : "forehead",
				"type" : "mid",
				"score" : NumberInt(61)
			},
			{
				"cls" : "nose",
				"type" : "oil",
				"score" : NumberInt(66)
			},
			{
				"cls" : "left_cheek",
				"type" : "oil",
				"score" : NumberInt(70)
			},
			{
				"cls" : "right_cheek",
				"type" : "mid",
				"score" : NumberInt(39)
			},
			{
				"cls" : "chin",
				"type" : "mid",
				"score" : NumberInt(61)
			}
		],
		"type" : "mid",
		"wiki" : "干性、中性和油性皮肤的分法，主要来自于皮脂分泌量的区别。\n中性皮肤：皮脂分泌量正常，皮肤角质层水含量正常（10-20%），皮肤紧致，有弹性，表面光滑润泽，细腻，是最理想的皮肤状态，一般只有婴幼儿和青少年才能拥有该类肤质。\n干性皮肤：皮脂分泌量低，皮肤角质层水含量低（<10%）,皮肤干燥脱屑，细腻但无光泽，肤色晦暗，易出现细小皱纹，色素沉着。\n油性皮肤：皮脂分泌量大，皮肤角质层含水量正常或者偏低，皮肤表面油腻，有光泽，毛孔粗大，易发生痤疮、毛囊炎。\n中性肌肤：皮肤皮脂腺和汗腺分泌较平衡，皮肤可以形成健康的皮脂末角质层保存适量的水分。但皮肤容易受到季节、环境、身体状况的影响而发生变化。\n混合性肌肤：在脸部的不同部位出现干性和油性的双重特征，皮肤虽也会出现夏季偏油、冬季偏干的状况，但T字区(前额、鼻翼和下巴)偏油，两颊偏干。",
		"tips" : "你属于中性偏油的皮肤。平时用35°的温水清洁，使用产品的清洁力略高，每2周可以做一次去角质。选用收敛控油的化妆水，选择带有控油功能的保湿乳液或者啫喱，尽量选择防晒乳液（防晒霜过于厚重），适当使用防晒喷雾，结合稍微控油的保湿，是你这类肤质的工作重点。"
	},
	"sensitive" : {
		"score" : NumberInt(1),
		"type" : "tolerance",
		"tips" : "无敏感情况，皮肤屏障功能良好，对寒冷、炎热、化妆品、酒精或药物等外界刺激无反应。平时合理清洁、适度保湿、加强防晒、保持合理水分即可。",
		"wiki" : "敏感性肌肤的特征\n1.皮肤表皮薄，皮脂分泌少，较干燥，微血管明显，皮肤呈现干燥机能减退，角质层保持水分的能力降低，肌肤表面的皮脂膜形成不完全。  \n2.接触化妆品或季节过敏后易引起皮肤过敏，出现红、肿、 痒。皮肤缺乏光泽，脸颊易充血红肿。  \n3.因季节变化而使皮肤容易呈现不稳定的状态。主要症状是搔痒、烧灼感、刺痛、皮肤发痒和出小疹子。  \n4.容易受冷风、食物、水质、紫外线、合成纤维、香味等外在环境或物质的影响。  \n5.单接触到刺激性物质就会引发肌肤的问题。对阳光、气候、水、植物（花粉）、化妆品、香水、蚊虫叮咬及高蛋白食物都有可能导致过敏。 "
	},
	"dark_circle" : {
		"_cls" : "ProblemObj",
		"problem_score" : NumberInt(65),
		"tips" : "你有混合型黑眼圈，平时可以通过在眼睛周围涂抹维生素E、K1和视黄醇混合物或者热敷来改善眼部血液循环。平时还要注意防晒，出门戴太阳镜、涂防晒霜，使用柔和的眼部化妆品，及时卸妆等来预防。还有注意不要熬夜、不要过度用眼，保证足够的睡眠，平时仰睡和不要用力揉眼都有利于缓解混合型黑眼圈。",
		"wiki" : "黑眼圈有三种：色素型，血管型、阴影型。\n色素型黑眼圈：日晒、眼周皮肤病、皮肤损伤、化妆品沉积等黑色素过度沉积引起眼圈周围颜色加深。\n血管型黑眼圈：眼睛周围的皮肤很薄，如果局部血液循环不好，血液中去氧的血红蛋白增多，血管通过眼睑皮肤透出青紫色，造成颜色黯淡。\n阴影型黑眼圈：眼睛周围的皮肤下垂、肌肉松弛、导致眼袋突出，造成局部阴影，让人看起来好像有很重的黑眼圈，其实是眼睛周围的结构发生变化，形成阴影，造成黑眼圈。",
		"type" : "HHX"
	},
	"pore" : {
		"_cls" : "ProblemObj",
		"problem_score" : NumberInt(29),
		"tips" : "你存在略微毛孔粗大的情况。对于外在皮肤护理，可使用深层清洁面乳、收缩毛孔爽肤水等产品定期控油；对于内在身体调理，要少吃油炸食品，多喝水，多吃蔬菜水果，保证适当运动和充足睡眠。",
		"wiki" : "毛孔粗大的原因来自于皮脂分泌旺盛，多余的油脂不能及时清除，进而堵塞毛孔，使毛孔膨胀，造成皮肤弹性松弛，最后毛囊粗大。此外，慢性复发性痤疮、性激素、抽烟喝酒、睡眠不足和不当皮肤护理都可影响毛孔大小。"
	},
	"wrinkle" : {
		"_cls" : "WrinkleObj",
		"problem_score" : NumberInt(11),
		"tips" : "你有轻微的眼下细纹，表现为皮纹加深，刚可辨认，似折痕虚。如因水份不足引起，请使用滋润眼霜轻轻按摩；如因眼过度引起，请不要过度使用眼睛，要经常放松，眺望远方；如因血液循环不佳引起，可以多运动，或者用发热眼罩等热敷。",
		"wiki" : "皱纹的形成：皮肤的正常衰老、皮肤附属器官功能的自然衰退、皮肤的新陈代谢减慢，使得真皮层的弹性纤维和胶原纤维逐渐老化，使皮肤的张力和弹力减弱；丰富的面部表情；长期的睡眠不足、皮肤缺水、不当的减肥、缺乏体育锻炼；化妆品的使用不当、烟酒的刺激。\n皱纹分为真性皱纹和假性皱纹。真性皱纹是面部形成的非手术或注射不能祛除的稳定性皱纹，此种皮肤的胶原纤维和弹力纤维性能下降，导致皮肤失去韧性和弹性；假性皱纹是面部出现的不稳定性的皱纹，是由于皮肤暂时性的缺水或缺乏油脂滋润引起的，这类皱纹可以通过皮肤弹性的自我调节或通过皮肤护理在一定时间内自行消退。\n\n",
		"filename" : "https://wechat-skin-v1-prod.oss-cn-shanghai.aliyuncs.com/results%2F2022-02-10%2FMTY0NDQ3NjYzNi43NzU3NzU0%2Fwrinkle_image.jpg?OSSAccessKeyId=LTAI4G8HUwXM84nxSgadaVLP&Expires=1644476941&Signature=pIi6uluXsnhv2rAXsiORKiz5bJo%3D",
		"category" : [
			{
				"cls" : "forehead",
				"problem_score" : NumberInt(0),
				"level" : "none"
			},
			{
				"cls" : "eyecorner",
				"problem_score" : NumberInt(3),
				"level" : "lightly"
			},
			{
				"cls" : "crowfeet",
				"problem_score" : NumberInt(0),
				"level" : "none"
			},
			{
				"cls" : "glabella",
				"problem_score" : NumberInt(0),
				"level" : "none"
			},
			{
				"cls" : "nasolabial",
				"problem_score" : NumberInt(89),
				"level" : "lightly"
			}
		]
	},
	"blackhead" : {
		"_cls" : "ProblemObj",
		"problem_score" : NumberInt(0),
		"tips" : "没有黑头，以预防为主。 少吃糖，少喝含糖饮料，比如奶茶，可乐；少吃盐，不要吃盐含量太高的食物；减轻自身压力，增加运动，调节工作节奏。",
		"wiki" : "黑头称开放性粉刺 ，主要是由皮脂、细胞屑和细菌组成的一种“栓”样物，阻塞在毛囊开口处而形成的，加上空气中的尘埃、污垢和氧化作用，使其接触空气的一头逐渐变黑，经氧化后成为黑色的小点，这些小点就是被称作黑头的油脂阻塞物。"
	},
	"roughness" : {
		"problem_score" : NumberInt(11),
		"tips" : "你的皮肤非常光滑，请继续保持哟。",
		"wiki" : "影响皮肤表面状态的粗燥与平滑度的因素很多，常见的有皮肤水分油分、斑点、纹理（皱纹）等。皮肤表面纹理细小、表浅，且走向柔和是青春美丽的皮肤外观。但随着年龄的增加和环境因素的影响，皮肤纹理会逐渐增大、增粗，皱纹形成并逐渐加深。"
	},
	"hyperpigmentations" : {
		"problem_score" : NumberInt(60),
		"dx_list" : [
			{
				"problem_score" : NumberInt(60),
				"cn_dx" : "黄褐斑",
				"formal_dx" : "黄褐斑",
				"wiki" : "黄褐斑也称肝斑，是面部对称性的黄褐色色素沉着斑。皮损常对称分布于颜面颧部及颊部而呈蝴蝶形，也可累计前额，鼻，口周或颏部。皮损为大小不一，边缘清楚的黄褐色或褐色斑片，日晒后色素加深，常在春夏季加重，无自觉症状，病程不定。多见于中青年女性，血中雌激素水平高是主要原因，其发病与妊娠、长期口服避孕药、月经紊乱有关。",
				"treatment" : [
					"治疗：尚无满意的疗法。如查出病因者尽量除去病因。由避孕药引起的黄褐斑，应停止服用，但短期内不一定消退。",
					"外用药物： 脱色剂如酪氨酸酶抑制剂软膏，如5%氢醌霜、2-4%曲酸霜及3%熊果苷等。维A酸/SOD/ 果酸等",
					"激光或强脉冲光治疗：光子嫩肤术及应用Q开关激光治疗黄褐斑部分患者有效。",
					"系统药物治疗：维生素C，维生素E，氨甲环酸",
					"预防：由于日晒与发病或病情加重有一定关系，故应注意防晒，外出时可外搽含避光剂的膏霜类或撑遮阳伞等。注意休息，避免熬夜精神紧张。"
				],
				"reference_image" : "https://app-skin-hdf-checkpoints.oss-cn-shanghai.aliyuncs.com/derms/facial_imgs/huang_he_ban.jpg?x-oss-process=image/resize,m_fill,h_240,w_240,limit_0"
			},
			{
				"problem_score" : NumberInt(34),
				"cn_dx" : "色素痣",
				"formal_dx" : "痣细胞痣（色素痣）",
				"wiki" : "色素痣是由痣细胞组成的良性新生物，又名痣细胞痣、细胞痣、黑素细胞痣、痣。本病常见，几乎每人都有，从婴儿期到年老者都可以发生，随年龄增长数目增加，往往青春发育期明显增多。女性的痣趋向比男性更多，白人的痣比黑人更多。偶见于黏膜表面。临床表现有多种类型。颜色多呈深褐或墨黑色，少数没有颜色的无色痣。本病属于发育畸形，黑素细胞在由神经嵴到表皮的移动过程中，由于偶然异常，造成黑素细胞的局部聚集而成。基本损害一般为直径<6mm的斑疹、丘疹、结节，疣状或乳头状，多为圆形，常对称分布，界限清楚，边缘规则，色泽均匀。数目多少不等，单个、数个甚至数十个，有些损害处可有一根至树根短而粗的黑毛。由于痣细胞的色素含量不同，临床上可呈棕色、褐色、蓝黑色、黑色或正常肤色、淡黄色、暗红色。日晒可增加暴露部位色素痣的数量。根据痣细胞的分布部位，分为交界痣、皮内痣和混合痣。",
				"treatment" : [
					"治疗：减少摩擦和外来因素损伤痣体。除美容需要外，一般不需要治疗。发生在掌跖、腰围、腋窝、腹股沟、肩部等易摩擦部位的色素痣应密切观察，特别是一些边缘不规则、颜色不均匀、直径≥1.5厘米的损害更应该注意。一旦发现迅速扩展或部分高起或破溃、出血时应及时切除。皮损较大的，手术切除后植皮；皮损较小且浅表者，可以给予二氧化碳激光治疗，治疗要彻底，否则残留痣细胞易复发。"
				],
				"reference_image" : "https://app-skin-hdf-checkpoints.oss-cn-shanghai.aliyuncs.com/derms/facial_imgs/se_su_zhi.jpeg?x-oss-process=image/resize,m_fill,h_240,w_240,limit_0"
			}
		]
	},
	"problem_bubbles" : [
		{
			"_cls" : "ProblemBubblesObj",
			"name" : "dark_circle",
			"score" : NumberInt(65)
		},
		{
			"_cls" : "ProblemBubblesObj",
			"name" : "hyperpigmentations",
			"score" : NumberInt(60)
		},
		{
			"_cls" : "ProblemBubblesObj",
			"name" : "pore",
			"score" : NumberInt(29)
		},
		{
			"_cls" : "ProblemBubblesObj",
			"name" : "wrinkle",
			"score" : NumberInt(11)
		},
		{
			"_cls" : "ProblemBubblesObj",
			"name" : "roughness",
			"score" : NumberInt(11)
		},
		{
			"_cls" : "ProblemBubblesObj",
			"name" : "blackhead",
			"score" : NumberInt(0)
		}
	],
	"acne" : {
		"category" : [ ]
	},
	"inflammations" : {
		"dx_list" : [ ]
	}
}
```
