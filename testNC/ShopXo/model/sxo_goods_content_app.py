# CREATE TABLE `sxo_goods_content_app` (
#   `id` int unsigned NOT NULL AUTO_INCREMENT COMMENT '自增id',
#   `goods_id` int unsigned NOT NULL DEFAULT '0' COMMENT '商品id',
#   `images` char(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL DEFAULT '' COMMENT '图片',
#   `content` text CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci COMMENT '内容',
#   `sort` tinyint unsigned DEFAULT '0' COMMENT '顺序',
#   `add_time` int unsigned DEFAULT '0' COMMENT '添加时间',
#   PRIMARY KEY (`id`) USING BTREE,
#   KEY `goods_id` (`goods_id`) USING BTREE,
#   KEY `sort` (`sort`) USING BTREE
# ) ENGINE=InnoDB AUTO_INCREMENT=1249 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci COMMENT='商品手机详情';