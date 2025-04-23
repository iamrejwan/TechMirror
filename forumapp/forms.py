from django import forms
from .models import Post, Category

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'category', 'tags', 'content']

    def __init__(self, *args, **kwargs):
        super(PostForm, self).__init__(*args, **kwargs)

        # Add help_text to fields
        self.fields['title'].help_text = 'Keep it short and descriptive.'
        self.fields['category'].help_text = 'Choose the most relevant category.'
        self.fields['tags'].help_text = 'Separate tags with commas.'
        self.fields['content'].help_text = 'Be detailed, but concise.'
    

        # Add Tailwind classes to form fields
        self.fields['title'].widget.attrs.update({
            'class': 'w-full px-4 py-2 border rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500',
            'placeholder': 'Enter a descriptive title'
        })
        self.fields['category'].widget.attrs.update({
            'class': 'w-full px-4 py-2 border rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500'
        })
        self.fields['tags'].widget.attrs.update({
            'class': 'w-full px-4 py-2 border rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500',
            'placeholder': 'e.g., javascript, react, frontend'
        })
        self.fields['content'].widget.attrs.update({
            'class': 'w-full px-4 py-2 border rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500',
            'rows': '12',
            'placeholder': 'Write your post content here...'
        
    def clean_title(self):
        title = self.cleaned_data.get('title')
        if len(title) < 10:
            raise forms.ValidationError("The title must be at least 10 characters long.")
        return title
})
