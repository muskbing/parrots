# -*- coding: utf-8 -*-
# Author: XuMing <xuming624@qq.com>
# Brief: 
from __future__ import print_function
from setuptools import setup, find_packages
from parrots import __version__

long_description = '''
## Usage

### install
* pip3 install parrots 
* Or 
```
git clone https://github.com/shibing624/parrots.git
cd pyrrots
python3 setup.py install
```


### speech recognition 
input:
```
import parrots

text = parrots.speech_recognition_from_file('./16k.wav')
print(text)

```

output:
```
北京图书馆
```

### tts
input:
```
import parrots

audio_file_path = parrots.synthesize('北京图书馆')
print(audio_file_path)

```

output:
```
北京图书馆 语音文件路径
```


'''

setup(
    name='parrots',
    version=__version__,
    description='Chinese Text To Speech and Speech Recognition',
    long_description=long_description,
    author='XuMing',
    author_email='xuming624@qq.com',
    url='https://github.com/shibing624/parrots',
    license="MIT License",
    classifiers=[
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Natural Language :: Chinese (Simplified)',
        'Natural Language :: Chinese (Traditional)',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
    keywords='TTS, chinese text to speech, speech',
    install_requires=[
        'pypinyin',
        'pydub',
        'pyaudio',
        'jieba'
    ],
    packages=find_packages(),
    package_dir={'parrots': 'parrots'},
    package_data={'parrots': ['*.*', 'data/*', 'utils/*', 'data/pinyin2hanzi/*', 'data/speech_model/*']}
)
