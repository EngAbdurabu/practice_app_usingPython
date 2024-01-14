"""
إنشاء مجلد جديد للمشروع:
mkdir {directory_name}
نضع مكان directory_name اسمًا مناسبًا للمجلد.

الانتقال إلى مجلد المشروع:
cd {directory_name}

إنشاء بيئة افتراضية:
python -m venv {env_name}
نضع مكان env_name اسم المجلد.

تثبيت الحزمة venv في توزيعة أوبنتو:
python3 -venv
تثبيت الحزمة venv في ديبيان و مشتقاته:
sudo apt install python3 -venv
استعراض المجلدات:
dir

تنشيط البيئة الافتراضية على نظام لينيكس أو ماك:
source venv/bin/activate

تنشيط البيئة الافتراضية على نظام ويندوز:
venv/scripts/activates

استعراض قائمة أوامر مدير الحزم pip:
pip

استعراض قائمة أوامر مدير الحزم pip في نظام لينيكس أو ماك:
pip3

استعراض الإصدار الحالي لمدير الحزم:
pip –version

تثبيت إطار العمل Flask:
pip install flask

استعراض الحزم المثبتة:
pip list

للاطلاع على معلومات حزمة معينة:
pip show {package_name}
نضع مكان package_name اسم الحزمة.

إنشاء ملف يحوي قائمة بأسماء الحزم وإصداراتها:
pip freeze > {file_name.txt}
نضع بدلًا من file_name اسم الملف.

تحديث إصدارات المكتبات المثبتة في المشروع:
pip install –upgrade -r {file_name.txt}

تثبيت الحزم الخاصة بالمشروع:
pip install -r {file_name.txt}

إلغاء تثبيت حزمة معينة:
pip uninstall {package_name}
نضع مكان package_name اسم الحزمة.

إلغاء تثبيت جميع الحزم المحددة ضمن ملف:
pip uninstall -r {file_name.txt}
"""
