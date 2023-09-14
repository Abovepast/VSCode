import sys
from you_get import common as youget  #导入you-get库
directory=r'mp4\\'
url='https://www.bilibili.com/video/BV1nu4y1X7Kn/?spm_id_from=333.1007.tianma.3-1-7.click&vd_source=481b69b23fa627d55c6ed8bb703fd3e1'
sys.argv=['you-get','-o',directory,'--format=mp4',url]
youget.main()
