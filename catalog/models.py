from django.db import models


# Create your models here.
class Genre(models.Model):
    """
    Model representing a book genre (e.g. Science Fiction, Non Fiction).
    """
    name = models.CharField(max_length=200, help_text="Enter a book genre (e.g. Science Fiction, French Poetry etc.)")

    def __str__(self):
        """
        String for representing the Model object (in Admin site etc.)
        """
        return self.name


""""这个模型用于存储关于书籍类别的信息。例如是否是小说或非小说，浪漫史或军事历史等。
如上所述，我们创建了Genre作为模型，而不是免费文本或选择列表，以便可以通过数据库管理可能的值，而不是硬编码。"""
