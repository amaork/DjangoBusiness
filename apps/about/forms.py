from django import forms


def generate_attr(name):
    return {'placeholder': "{0:s}".format(name), 'class': 'form-control'}


class UserCommentForm(forms.Form):
    action = 'comment'

    name = forms.CharField(label="", widget=forms.TextInput(attrs=generate_attr('名字')), max_length=32)
    phone = forms.CharField(label="", widget=forms.TextInput(attrs=generate_attr('电话')), max_length=11)
    wechat = forms.CharField(label="", widget=forms.TextInput(attrs=generate_attr('微信')), max_length=11)

    comment_attr = generate_attr('留言')
    comment_attr['rows'] = '5'
    comment = forms.CharField(label="", widget=forms.Textarea(attrs=comment_attr), max_length=128)

