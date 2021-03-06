#
# Copyright (C) 2021-2022 by TeamYukki@Github, < https://github.com/TeamYukki >.
#
# This file is part of < https://github.com/TeamYukki/YukkiMusicBot > project,
# and is released under the "GNU v3.0 License Agreement".
# Please see < https://github.com/TeamYukki/YukkiMusicBot/blob/master/LICENSE >
#
# All rights reserved.

HELP_1 = """✅**<u>اوامر الادمنيه:</u>**

c ضع الحرف قبل الامر لتنفيذه في المجموعة.

/pause أو /cpause - توقف الموسيقى المُشغلة.
/seek [ عدد ثواني ] - للتقدم في الاغنية حسب الوقت المعطى
/seekback [ عدد الثواني ] - للعودة في الاغنية حسب الوقت المعطى 
/resume or /cresume- استئناف الموسيقى المشغلة.
/mute or /cmute- كتم صوت الموسيقى.
/unmute or /cunmute- الغاء الكتم عن البوت.
/skip or /cskip- التخطي للاغنية التالية في قائمة التشغيل.
/stop or /cstop- ايقاف كل الاغاني.
/shuffle or /cshuffle- ترتيب عشوائي للاغاني في قائمة التشغيل.

✅--**التخطي المحدد:**--
/skip or /cskip [رقم (مثلا : 3)] 
    - يتخطى الموسيقى إلى الرقم المحدد في قائمة الانتظار.  مثال: سيتخطى / skip 3 الموسيقى إلى الموسيقى في قائمة الانتظار الثالثة ويتجاهل الموسيقى 1 و 2 في قائمة الانتظار

✅--**وضع الحلقة:**--
/loop or /cloop [enable/disable] or [رقم بين  1-10] 
    - عند التنشيط ، يقوم البوت بتكرار تشغيل الموسيقى الحالية إلى 1-10 مرات في الدردشة الصوتية.  افتراضي إلى 10 مرات.

"""
AUTH_TEXT = """
✅--**اوامر المعتمدين:**--
المستخدمين المعتمدون سيستطيعون استخدام جميع اوامر المشرفين بدون رفعهم مشرف في المجموعة 
/auth [اليوزر] - اضف شخص لقائمة المعتمدين.
/unauth [اليوزر] - لحذف شخص من القائمة.
/authusers - جلب قائمة المعتمدين."""


HELP_2 = """✅<u>**تشغيل الأوامر:**</u>

الأوامر المتوفرة = play , vplay , cplay

أوامر ForcePlay = playforce , vplayforce , cplayforce

**c** للتشغيل في القناة.
**v** لتشغيل الفيديو.

/play او /vplay او /cplay  - سيبدأ البوت في تشغيل طلبك المحدد على المكالمه .

/channelplay [معرف القناة او الايدي] او [Disable] - قم بتوصيل القناة بمجموعة وشغل الموسيقى على الدردشة الصوتية للقناة من مجموعتك.


✅**<u>قوائم تشغيل سيرفر البوت :</u>**
/playlist  - تحقق من قائمة التشغيل المحفوظة على الخوادم.
/deleteplaylist - احذف أي موسيقى محفوظة في قائمة التشغيل الخاصة بك
/play  - ابدأ تشغيل قائمة التشغيل المحفوظة من الخوادم."""


HELP_3 = """✅<u>**أوامر البوت:**</u>

/stats - احصل على أفضل 10 اغاني للإحصائيات العالمية ، أفضل 10 مستخدمين للروبوت ، أفضل 10 محادثات على الروبوت ، أفضل 10 تم تشغيلها في محادثة ، إلخ.

/sudolist - تحقق من المطورين 

/lyrics [اسم الاغنية] - لجلب كلمات الاغنية من الويب.

/song [اسم المقطع] او [الرابط] - قم بتنزيل أي مقطع صوتي من بتنسيقات mp3 أو mp4.

/player -  احصل على لوحة لعب تفاعلية.

/queue or /cqueue-تحقق من قائمة انتظار الموسيقى."""

HELP_4 = """✅<u>**أوامر اضافية:**</u>

/start - بدأ تشغيل البوت.
/help  - للمساعدة في اوامر البوت .
/speedtest - معرفة سرعة البوت .

✅ اعدادات المجموعة:
/settings - لجلب خيار الاعدادات 

🔗 الخيارات:
1️⃣ يمكنك ضبط  جودة التي تريد بثها على الدردشة الصوتية..
2️⃣ يمكنك ضبط جودة الفيديو التي تريد بثها في الاتصال .
3️⃣ المعتمدين :- يمكنك تغيير وضع أوامر المسؤول من هنا للجميع أو للمسؤولين فقط.  إذا كان كل شخص موجودًا في مجموعتك ، فسيكون قادرًا على استخدام أوامر المسؤول (مثل /skip /stop الخ...)
4️⃣ وضع التنظيف: عند التمكين ، يحذف رسائل الروبوت بعد 5 دقائق من مجموعتك للتأكد من بقاء محادثتك نظيفة وجيدة.
5️⃣ تنظيف الاوامر : عند التمكين سيحذف الاوامر المعطاة له مباشرة من الادمن بعد تنفيذها مثل  (play, /pause, /shuffle, /stop / الخ ...) مباشرة .
6️⃣ اعدادات التشغيل:
/playmode - احصل على لوحة إعدادات تشغيل كاملة مع أزرار حيث يمكنك ضبط إعدادات تشغيل مجموعتك. 
الخيارات فيها:
1️⃣ وضع البحث [مباشر او انلاين] - غير حسب ما تريده من ترسل الامر  /play . 
2️⃣ اوامر الادمن [الجميع لو بس الادمن ] - اذا الحميع راح الكل يكدر يستخدم الاوامر اما اذا الادمنز بس يعني المشرفين فقط يتحكمون باوامر (مثل skip /stop/  الخ ...)
3️⃣ اوامر التشغيل [الكل لو الادمن ] - اذا ادمن بس الادمنية يكدرون يشغلون الاغاني اما اذا الجميع الكل عادي ."""

HELP_5 = """🔰**<u>اضافة وازالة المطورين :</u>**

/addsudo [اسم المستخدم أو الرد على المستخدم]
/delsudo [اسم المستخدم أو الرد على المستخدم ]

🤖 اوامر البوت :
/reboot - أعد تشغيل البوت الخاص بك. 
/update - تحديث البوت.
/speedtest - تحقق من سرعات الخادم
/maintenance [enable/disable] 
/logger [enable/disable] -يقوم البوت بتسجيل الاستعلامات التي تم البحث عنها في مجموعة المسجل.
/autoend [enable/disable] - قم بتمكين إنهاء البث التلقائي بعد 3 دقائق إذا لم يكن هناك من يستمع.

📈 الاحصائيات:
/activevoice - تحقق من المكالمات المشغلة في البوت.
/activevideo - تحقق من الفيديوهات المشغلة في البوت.
/stats - تحقق من معلومات البوت

⚠️ امر القائمة السوداء:
/blacklistchat [ايدي المجموعة] - ( ضع أي دردشة في القائمة السوداء ( محظورة من استخدام البوت
/whitelistchat [ايدي المجموعة] - أضف إلى القائمة البيضاء أي دردشة في القائمة السوداء من استخدام البوت
/blacklistedchat -تحقق من جميع الدردشات المدرجة في القائمة السوداء.

👤اوامر الحظر :
( ينحظر من استخدام البوت فقط يعني يبقة موجود بالكروب بس من ينطي أمر للبوت راح يلبسه ) 

/block [المعرف أو الايدي] - يمنع المستخدم من استخدام أوامر البوت في هذه المجموعة .
/unblock [المعرف أو الايدي] - قم بإزالة مستخدم من قائمة المحظورين .
/blockedusers -تحقق من قائمة المحظورين 

👤 اوامر الحظر العام :

( ينحظر من استخدام البوت فقط يعني يبقة موجود بالكروب بس من ينطي أمر للبوت راح يلبسه ) 

/gban [المعرف أو الايدي] - Gban يمنع المستخدم من استخدام اوامر البوت في كل المجموعات .
/ungban [المعرف أو الايدي] - لإزالة مستخدم من القائمه 
/gbannedusers - تحقق من القائمه

🎥 اوامر مكالمات الفيديو:
/set_video_limit [رقم المجموعات] - قم بتعيين الحد الأقصى لعدد الدردشات المسموح به لمكالمات الفيديو في المرة الواحدة. افتراضي إلى 3 محادثات.

⚡️اوامر البوت الخاص:
 البوت حيكون خاص بيك ومحد يكدر يفعلة بس أنت 
/authorize [ايدي المجموعة] - اسمح بالمحادثة لاستخدام البوت الخاص بك.
/unauthorize [ايدي المجموعة] - عدم السماح للدردشة باستخدام الروت الخاص بك.
/authorized - تحقق من جميع الدردشات المسموح بها من البوت الخاص بك.

🌐 اوامر الاذاعة:
/broadcast [رسالة أو بالرد على الرسالة] - قم ببث أي رسالة إلى الدردشات اللتي فعلت البوت.

اوامر للاذاعه:
-pin : سيؤدي هذا إلى تثبيت رسالتك
-pinloud : سيؤدي هذا إلى تثبيت رسالتك بإشعار عالٍ
-user : سيؤدي هذا إلى بث رسالتك للمستخدمين الذين بدأوا برنامج الروبوت الخاص بك.
-assistant : سيؤدي هذا إلى بث رسالتك من حساب المساعد الخاص بالبوت الخاص بك.
-nobot : سيؤدي هذا إلى إجبار الروبوت الخاص بك على عدم بث الرسالة

مثال: /broadcast -user -pin صلِ على النبي ♥️

"""
