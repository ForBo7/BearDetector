# AUTOGENERATED! DO NOT EDIT! File to edit: app.ipynb.

# %% auto 0
__all__ = ['learner', 'cats', 'img', 'lbl', 'examples', 'title', 'description', 'article', 'interface', 'classify_img']

# %% app.ipynb 3
from fastai.vision.all import *
import gradio as gr

# %% app.ipynb 6
learner = load_learner('model/export.pkl')

# %% app.ipynb 9
cats = ('Black Bear', 'Grizzly Bear', 'Teddy Bear',)

def classify_img(img):
    preds, idx, probs = learner.predict(img)
    return dict(zip(cats, map(float, probs)))

# %% app.ipynb 12
img = gr.Image()
lbl = gr.Label()
examples = [str(img_path) for img_path in Path('example_images/').rglob('*.jpg')]

title = 'Bear Classifier'
description = 'My first AI model that can tell you whether an image contains a grizzly bear, a black bear, or a teddy bear. This model was trained on the ' \
              'ResNet18 architecture and used the fastai library. Check out the associated blog post with the link below!'
article = """
<p style='text-align: center; font-size: 36px'><a href='https://forbo7.github.io/forblog/posts/2_bear_classifier_model.html'>Blog Post</a></p>
"""

# %% app.ipynb 15
interface = gr.Interface(
    fn=classify_img,
    inputs='image',
    outputs='label',
    examples=examples,
    title=title,
    description=description,
    article=article
)

interface.launch(inline=False, enable_queue=True)
