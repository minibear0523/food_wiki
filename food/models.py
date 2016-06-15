# encoding=UTF-8
from __future__ import unicode_literals
from django.db import models


class FoodModel(models.Model):
    FOOD_CATEGORY_CHOICES = (
        ('VE', '蔬菜'),
        ('MU', '蘑菇'),
        ('BE', '豆类'),
        ('FR', '水果'),
        ('NU', '坚果及植物油'),
        ('HE', '药草和调味料'),
        ('GR', '谷物'),
        ('ME', '肉,海鲜和乳制品'),
        ('DR', '饮料和零食'),
        ('NS', '营养补充品'),
    )

    SUB_CATEGORY_CHOICES = (
        ('Vegetable', (
                ('LE', '叶子,花朵和茎类蔬菜'),
                ('FU', '果实和豆类蔬菜'),
                ('RO', '根类,球茎类和块茎类蔬菜'),
            )
        ),
        ('Fruit', (
                ('CI', '柑橘属植物'),
                ('NU', '核果'),
                ('PO', '梨果'),
                ('TF', '热带水果'),
                ('SP', '蔓生果'),
                ('BE', '浆果'),
            )
        ),
        ('Meat', (
                ('ME', '肉'),
                ('SF', '海鲜'),
                ('DA', '乳制品和鸡蛋'),
            )
        ),
        ('Drink', (
                ('DR', '饮料'),
                ('SN', '零食'),
            )
        )
    )

    name = models.CharField(max_length=200, verbose_name='名称')
    category = models.CharField(max_length=2, choices=FOOD_CATEGORY_CHOICES, verbose_name='分类')
    sub_category = models.CharField(max_length=2, choices=SUB_CATEGORY_CHOICES, null=True, verbose_name='子分类')
    origin_country = models.CharField(max_length=200, verbose_name='原产地')
    season = models.CharField(max_length=200, verbose_name='季节')
    value = models.TextField(verbose_name='营养价值')
    unit_weight = models.FloatField(default=0.0, verbose_name='单位重量(g)')
    calories = models.FloatField(default=0.0, verbose_name='卡路里')
    protein = models.FloatField(default=0.0, verbose_name='蛋白质')
    full_fat = models.FloatField(default=0.0, verbose_name='全脂肪')
    saturated_fat = models.FloatField(default=0.0, verbose_name='饱和脂肪')
    carbohydrates = models.FloatField(default=0.0, verbose_name='碳水化合物')
    cellulose = models.FloatField(default=0.0, verbose_name='纤维素')
    usage = models.TextField(null=True, verbose_name='充分利用')
    efficacy = models.TextField(null=True, verbose_name='功效')

    def __str__(self):
        return ":".join([self.category, self.name])

    class Meta:
        verbose_name = '食物'
        verbose_name_plural = '食物'
