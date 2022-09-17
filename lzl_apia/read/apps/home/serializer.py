from rest_framework import serializers
from . import models


class SerializerAuthor(serializers.ModelSerializer):
    class Meta:
        model = models.Author
        fields = '__all__'


# 书籍分类
class SerializerTag(serializers.ModelSerializer):
    class Meta:
        model = models.Tag
        fields = '__all__'


# 所有书序列化类
class SerializerBooks(serializers.ModelSerializer):
    author = SerializerAuthor()
    tag = SerializerTag()

    # same_type = serializers.CharField()
    class Meta:
        model = models.Book
        fields = [
            'id',
            'name',
            'book_img',
            'desc',  # 简介
            'author',  # 子序列化
            'click_num',  # 点击数
            'zhangjie',  # 章节
            'tag',
            'gender_type',  # 男女频道
            'create_time',
            'bookzj',
            'comment_num',  # 书的评论数量
            'same_type',
        ]


# 频道
class SerializerGender(serializers.ModelSerializer):
    class Meta:
        model = models.Gender
        fields = ['id', 'gender', 'gender_name']


# 章节详情
class SerializerDetail(serializers.ModelSerializer):

    class Meta:
        model = models.BookZhangjie
        fields = '__all__'

    ZJ_id = serializers.CharField()
    # num = serializers.IntegerField()


from rest_framework.exceptions import APIException


class ZhangjieDetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.ZhangjieDetail
        fields = '__all__'

    zj_name = serializers.CharField()
    # zj_book = serializers.CharField(read_only=True)


# from apps import user

# 评论
class SerializerComment(serializers.ModelSerializer):
    class Meta:

        model = models.Comment
 
        fields = '__all__'

    # user = serializers.CharField(read_only=True)

    # user_list = serializers.PrimaryKeyRelatedField(queryset=usera.models.objects.all(),many=True)
    user_list = serializers.ListField(write_only=True, allow_null=True)

    username = serializers.CharField(read_only=True)

    nickname = serializers.CharField(read_only=True)

    user_img = serializers.CharField(read_only=True)

    parent_user = serializers.CharField(read_only=True)

    bookname = serializers.CharField(read_only=True)

    # def validate(self, attrs):
    #
    #     print(attrs)
    #
    #     return attrs
    # 评论提交
    def create(self, validated_data):

        # 拿到用户名
        user_id = validated_data.get('user').id

        # print(validated_data.get('user_list'))
        # print(type(validated_data.get('user_list')))
        # print(user_id.id)
        # print(validated_data)
        # 拿到评论内容
        context = validated_data.get('context')
        # print(validated_data.get('book').id)
        # 判断评论内容是否为空
        if context:

            # 拿到回复人的列表ID
            user_list = validated_data.get('user_list')
            user_list = list(set(user_list))

            # 拿到此次评论的次数
            num = models.Comment.objects.last().com_num + 1
            # print(num)

            # 判断是否拿到了ID，如果拿到，说明回复了用户
            if user_list:

                comment_obj = ''

                for obj in user_list:
                    comment_obj = models.Comment.objects.create(parent_id=obj,
                                                                book=validated_data.get('book'),
                                                                context=context,
                                                                user_id=user_id,
                                                                com_num=num)
                comment_obj.book.comment_num = comment_obj.book.comment_num+1
                comment_obj.book.save()

                return comment_obj

            else:
                comment_obj = models.Comment.objects.create(book=validated_data.get('book'),
                                                            context=context,
                                                            user_id=user_id,
                                                            com_num=num)

                comment_obj.book.comment_num = comment_obj.book.comment_num + 1
                comment_obj.book.save()
                return comment_obj
        else:

            raise APIException({'detail': '请输入内容后提交评论！'})

    # same_type = serializers.CharField()


# 轮播图
class SerializerBanner(serializers.ModelSerializer):
    class Meta:
        model = models.Banner
        fields = '__all__'


# 章节内容详情
class ZhangjieDetail(serializers.ModelSerializer):
    class Meta:
        model = models.ZhangjieDetail
        fields = '__all__'


# 书架的序列化
class ShujiaSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.ShuJia
        fields = '__all__'

    bookname = serializers.CharField(read_only=True)

    def create(self, validated_data):
        user = validated_data.get('user')
        book = validated_data.get('book')

        obj = models.ShuJia.objects.filter(user=user, book=book)

        if obj:

            raise APIException({'detail':'这本书已经添加到书架了'})

        res = super().create(validated_data)

        return res

