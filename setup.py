from distutils.core import setup


setup(
  name = 'akmathpy',        
  packages = ['akmathpy'],   
  version = '1.0',      
  license='MIT',              
description = 'liabrary to check Armgstrong,prime,palindrome number and palindrome String',   
  author = 'Abhijeet Khatri',                   
  author_email = 'abhijeetkhatri@gmail.com',      
  url = 'https://github.com/AbhijeetJK/akmathpy.git',
download_url ='https://github.com/AbhijeetJK/akmathpy/archive/1.0.0.tar.gz',  
  keywords = ['math', 'armgstrong', 'palindrome','prime'],   
  install_requires=[            
          'akmathpy',
      ],
  classifiers=[
    'Development Status :: 3 - Alpha',     
    'Intended Audience :: Developers',      
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',  
    'Programming Language :: Python :: 3',      
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
  ],
)
