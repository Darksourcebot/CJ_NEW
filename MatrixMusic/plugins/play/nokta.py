#Tepthon
import random
from pyrogram import Client, filters
from pyrogram.types import Message
from strings.filters import command
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from typing import Union
from MatrixMusic import app


@app.on_message(command("احكام"))
async def bottttt(client, message):
    selections = [" ※ صورة وجهك او رجلك او خشمك او يدك ؟ ",
" ※ اصدر اي صوت يطلبه منك الاعبين ؟ ",
" ※ سكر خشمك و قول كلمة من اختيار الاعبين الي معك ؟ ",
" ※ روح الى اي قروب عندك في الواتس اب و اكتب اي شيء يطلبه منك الاعبينالحد الاقصى 3 رسائل ؟ ",
" ※ قول نكتة ولازم احد الاعبين يضحك اذا ضحك يعطونك ميوت الى ان يجي دورك مرة ثانية ؟ ",
" ※ سمعنا صوتك و غن اي اغنية من اختيار الاعبين الي معك ؟ ",
" ※ ذي المرة لك لا تعيدها ؟ ",
" ※ ارمي جوالك على الارض بقوة و اذا انكسر صور الجوال و ارسله في الشات العام ؟ ",
" ※ صور اي شيء يطلبه منك الاعبين ؟ ",
" ※ اتصل على ابوك و قول له انك رحت مع بنت و احين هي حامل.... ؟ ",
" ※ سكر خشمك و قول كلمة من اختيار الاعبين الي معك ؟ ",
" ※ اعطي اي احد جنبك كف اذا مافيه احد جنبك اعطي نفسك و نبي نسمع صوته ؟ ",
" ※ ارمي جوالك على الارض بقوة و اذا انكسر صور الجوال و ارسله في الشات العام ؟ ",
" ※ روح عند اي احد بالخاص و قول له انك تحبه و الخ ؟ ",
" ※ اكتب في الشات اي شيء يطلبه منك الاعبين في الخاص ؟ ",
" ※ قول نكتة اذا و لازم احد الاعبين يضحك اذا محد ضحك يعطونك ميوت الى ان يجي دورك مرة ثانية ؟ ",
" ※ سامحتك خلاص مافيه عقاب لك  ؟ ",
" ※ اتصل على احد من اخوياكخوياتك , و اطلب منهم مبلغ على اساس انك صدمت بسيارتك ؟ ",
" ※ غير اسمك الى اسم من اختيار الاعبين الي معك ؟ ",
" ※ اتصل على امك و قول لها انك تحبها  ؟ ",
" ※ لا يوجد سؤال لك سامحتك  ؟ ",
" ※ قل لواحد ماتعرفه عطني كف ؟ ",
" ※ منشن الجميع وقل انا اكرهكم ؟ ",
" ※ اتصل لاخوك و قول له انك سويت حادث و الخ.... ؟ ",
" ※ روح المطبخ و اكسر صحن  ؟ ",
" ※ اعطي اي احد جنبك كف اذا مافيه احد جنبك اعطي نفسك و نبي نسمع صوت الكف ؟ ",
" ※ قول لاي بنت موجود في الروم كلمة حلوه ؟ ",
" ※ تكلم باللغة الانجليزية الين يجي دورك مرة ثانية لازم تتكلم اذا ما تكلمت تنفذ عقاب ثاني ؟ ",
" ※ لا تتكلم ولا كلمة الين يجي دورك مرة ثانية و اذا تكلمت يجيك باند لمدة يوم كامل من السيرفر ؟ ",
" ※ قول قصيدة  ؟ ",
" ※ تكلم باللهجة السودانية الين يجي دورك مرة ثانية ؟ ",
" ※ اتصل على احد من اخوياكخوياتك , و اطلب منهم مبلغ على اساس انك صدمت بسيارتك ؟ ",
" ※ اول واحد تشوفه عطه كف ؟ ",
" ※ سو مشهد تمثيلي عن اي شيء يطلبه منك الاعبين ؟ ",
" ※ سامحتك خلاص مافيه عقاب لك  ؟ ",
" ※ اتصل على ابوك و قول له انك رحت مع بنت و احين هي حامل.... ؟ ",
" ※ روح اكل ملح + ليمون اذا مافيه اكل اي شيء من اختيار الي معك ؟ ",
" ※ تاخذ عقابين ؟ ",
" ※ قول اسم امك افتخر بأسم امك ؟ ",
" ※ ارمي اي شيء قدامك على اي احد موجود او على نفسك ؟ ",
" ※ اذا انت ولد اكسر اغلى او احسن عطور عندك اذا انتي بنت اكسري الروج حقك او الميك اب حقك ؟ ",
" ※ اذهب الى واحد ماتعرفه وقل له انا كيوت وابي بوسه ؟ ",
" ※ تتصل على الوالدهو تقول لها خطفت شخص ؟ ",
" ※ تتصل على الوالدهو تقول لها تزوجت با سر ؟ ",
" ※ اتصل على الوالدهو تقول لهااحب وحده ؟ ",
" ※ تتصل على شرطي تقول له عندكم مطافي ؟ ",
" ※ خلاص سامحتك ؟ ",
" ※ تصيح في الشارع انامجنوون ؟ ",
" ※ تروح عند شخص وقول له احبك ؟"]
    bar = random.choice(selections)
    await message.reply_text(bar)


@app.on_message(command("نكته"))
async def bottttt(client, message):
    selections = ["واحد مشغول أتجوز واحدة مشغولة خلفوا عيل مش فاضيلهم 👻😹",
"اتنين اغبياء واحد منهم لقى كنز من الفلوس دفنها وكتب مكانها مفيش هنا أي فلوس قام الغبي التاني أخد الفلوس وكتب أنا محفرتش هنا ومخدتش حاجة 👻😹", 
"لما بعمل دايت باكل باكل نفس الاكل بس وانا مكسوف من نفسي اتمنى يكون دا بيحرق كالوريز 👻😹",
"واحد غبي حب يدلع مراته سألها قالها كم وزنك قالتله  40 قالها الله نفس مقاس جزمتي 👻😹", 
"مره واحد قابل اتنين وهو ماشي بقوا تلاته 👻😹",
"مرة أصالة شحنت كارت فكة جالها 60 دقيقة حياة 👻😹" , 
"مرة كتاب عطش جابوله book مايه 👻😹" ,
"مرة واحدة اسمها نهلة كبرت بقت دبانة 👻😹" , 
"مرة واحد شاف كوتشي العربية نام غطاه👻😹" , 
"مرة واحد اسمه حمدي ولما كبر بقا هبصم 👻😹" , 
"لما ابعت لحد مسدج ويعمل seen وميردش بحذفها من عندي على اساس اني كدا برد كرامتي يعني 👻😹" , 
"لو عملو جزء تاني من مسلسل شمس الزناتي هيسموه شمس الزنة الجاية 👻😹" , 
"مرة واحد جاب طاجن لاحما ومجبش لمحما 👻😹" , 
"لا بص عايزك تسيب فعلك وتمسك في رد فعلي قماشته احلي 👻😹" , 
"مرة واحد سال واحدة قالها اسمك اي قالتلو دارين قالها وانا غرفتين وصالة 👻😹" , 
"مرة واحد سال واحدة قالها اسمك اي قالتلو دارين قالها وانا غرفتين وصالة 👻😹" , 
"مرة واحد مسطول طلب من صاحبه المسطول يمشي على دخان السجارة.. قال له أنت عبيط؟ افرض طفيت السجارة اقع 👻😹", 
" مهندس برمجة اتجوز وخلف بنتين توأم.. سمى واحدة لوجين والتانية Log out 👻😹", 
"مهندس برمجة اتجوز وخلف بنتين توأم.. سمى واحدة لوجين والتانية Log out 👻😹" , 
"طفولتي ضاعت وانا بعد الكشكول ابو 60 ورقه عشان اشوف الشركة نصابة ولا لا 👻😹", 
"واحد ماشي ورا وحدة قالها الحلوة وراها مشوار؟ قالت لا.. الحلوة وراها حمار 👻😹" , 
"واحد مشغول أتجوز واحدة مشغولة خلفوا عيل مش فاضيلهم 👻😹",
"مرة القمر كان عايز يتجوز الشمس قالتله أتجوز واحد صايع طول الليل 👻😹",
"ولد بيسأل أبوه هو الحب أعمى رد عليه أبوه بص في وش أمك وأنت تعرف 👻😹",
"مرة مفتاح مات أهله ما زعلوش عليه عشان معاهم نسخة تانية 👻😹",
"ممرضة خلفت توأم سمت واحد عضل والتاني وليد 👻😹",
"مسطول أتجوز صينية قالتله مالك ساكت ليه؟ قالها مش عارف افتكرتك نايمة 👻😹",
"واحدة نجومة جوزها رماها من الدور الثالث طلعتله وقالتله بلاش الهزار البايخ ده 👻😹",
"اتنين مساطيل حبوا يسرقوا عمارة فقالوا لبعض إحنا ناخد العمارة بعيد ونسرقها برحتنا 👻😹",
"منهم بص ورا ملقاش الهدوم فقال له كفاية كدة احنا بعدنا أوى 👻😹",
"حر جدًا، قالتله مفيش مشكلة نطلعها بالليل 👻😹",
"واحد رجع في كلامه خبط اللي وراه 👻😹",
"واحد خلقه ضاق أعطاه لأخوه الصغير 👻😹",
"مرة مدرس رياضيات خلف ولدين واستنتج التالت 👻😹",
"واحد كهربائي أتجوز أربعة جابلهم مشترك 👻😹",
"كفايه عليك كده ياد يبن الحلوهه 👻😹",
"واحدة اسمها ساندي دخلت هندسة بقت ساندي متر مربع 👻😹",
"مرة شرطي مرور خلّف ولد بيتكلم بالإشارة 👻😹",
"مره واحد اسمو شادو  كان بيرجم ابليس ف الحج قالولو ليه؟ قال عشان يمكن احتاجو 👻😹",
"ﻣﺮه واﺣﺪ ﻣﺴﻄﻮل ﻣﺎﺷﻰ ﻓﻰ اﻟﺸﺎرع ﻟﻘﻰ مذﻳﻌﻪ ﺑﺘﻘﻮﻟﻪ ﻟﻮ ﺳﻤﺤﺖ ﻓﻴﻦ اﻟﻘﻤﺮ ﻗﺎﻟﻬﺎ اﻫﻮه ﻗﺎﻟﺘﻠﻮ ﻣﺒﺮوك ﻛﺴﺒﺖ ﻋﺸﺮﻳﻦ ﺟﻨﻴﻪ ﻗﺎﻟﻬﺎ ﻓﻰ واﺣﺪ ﺗﺎﻧﻰ ﻫﻨﺎك اﻫﻮه  👻😹",
"واحد بيشتكي لصاحبه بيقوله أنا مافيش حد بيحبني ولا يفتكرني أبدًا، ومش عارف أعمل إيه قاله سهلة استلف من الناس فلوس هيسألوا عليك كل يوم 👻😹",
" مرة واحد مصري دخل سوبر ماركت في الكويت عشان يشتري ولاعة راح عشان يحاسب بيقوله الولاعة ديه بكام قاله دينار قاله منا عارف ان هي نار بس بكام 👻😹",
"بنت حبت تشتغل مع رئيس عصابة شغلها في غسيل الأموال 👻😹",
"واحد بيشتكي لصاحبه بيقوله أنا مافيش حد بيحبني ولا يفتكرني أبدًا، ومش عارف أعمل إيه قاله سهلة استلف من الناس فلوس هيسألوا عليك كل يوم 👻😹",
"ﻣﺮه واﺣﺪ ﻣﺴﻄﻮل ﻣﺎﺷﻰ ﻓﻰ اﻟﺸﺎرع ﻟﻘﻰ مذﻳﻌﻪ ﺑﺘﻘﻮﻟﻪ ﻟﻮ ﺳﻤﺤﺖ ﻓﻴﻦ اﻟﻘﻤﺮ؟ ﻗﺎﻟﻬﺎ اﻫﻮه ﻗﺎﻟﺘﻠﻮ ﻣﺒﺮوك ﻛﺴﺒﺖ ﻋﺸﺮﻳﻦ ﺟﻨﻴﻪ ﻗﺎﻟﻬﺎ ﻓﻰ واﺣﺪ ﺗﺎﻧﻰ ﻫﻨﺎك اﻫﻮه 👻😹",
"واحده ست سايقه على الجي بي اي قالها انحرفي قليلًا قلعت الطرحة 👻😹",
"مرة واحد غبي معاه عربية قديمة جدًا وبيحاول يبيعها وماحدش راضي يشتريها.. راح لصاحبه حكاله المشكلة صاحبه قاله عندي لك فكرة جهنمية هاتخليها تتباع الصبح أنت تجيب علامة مرسيدس وتحطها عليها. بعد أسبوعين صاحبه شافه صدفة قاله بعت العربية ولا لاء؟ قاله انت  مجنون حد يبيع مرسيدس 👻😹",
"مره واحد بلديتنا كان بيدق مسمار فى الحائط فالمسمار وقع منه فقال له :تعالى ف مجاش, فقال له: تعالي ف مجاش. فراح بلديتنا رامي على المسمار شوية مسمامير وقال: هاتوه 👻😹",
"واحدة عملت حساب وهمي ودخلت تكلم جوزها منه ومبسوطة أوي وبتضحك سألوها بتضحكي على إيه قالت لهم أول مرة يقول لي كلام حلو من ساعة ما اتجوزنا 👻😹",
"بنت حبت تشتغل مع رئيس عصابة شغلها في غسيل الأموال 👻😹",
"مره واحد اشترى فراخ علشان يربيها فى قفص صدره 👻😹",
"مرة واحد من الفيوم مات اهله صوصوا عليه 👻😹",
"ﻣﺮه واﺣﺪ ﻣﺴﻄﻮل ﻣﺎﺷﻰ ﻓﻰ اﻟﺸﺎرع ﻟﻘﻰ مذﻳﻌﻪ ﺑﺘﻘﻮﻟﻪ ﻟﻮ ﺳﻤﺤﺖ ﻓﻴﻦ اﻟﻘﻤﺮ ﻗﺎﻟﻬﺎ اﻫﻮه ﻗﺎﻟﺘﻠﻮ ﻣﺒﺮوك ﻛﺴﺒﺖ ﻋﺸﺮﻳﻦ ﺟﻨﻴﻪ ﻗﺎﻟﻬﺎ ﻓﻰ واﺣﺪ ﺗﺎﻧﻰ ﻫﻨﺎك اﻫﻮه 👻😹",
"مره واحد شاط كرة فى المقص اتخرمت. 👻😹",
"مرة واحد رايح لواحد صاحبهفا البواب وقفه بيقول له انت طالع لمين قاله طالع أسمر شوية لبابايا قاله يا أستاذ طالع لمين في العماره 👻😹",
" وهه عاوز تانيي 👻😹",                  
"مرة القمر كان عايز يتجوز الشمس قالتله أتجوز واحد صايع طول الليل 👻😹",
"ولد بيسأل أبوه هو الحب أعمى رد عليه أبوه بص في وش أمك وأنت تعرف 👻😹",
"مرة مفتاح مات أهله ما زعلوش عليه عشان معاهم نسخة تانية 👻😹",
"ممرضة خلفت توأم سمت واحد عضل والتاني وليد 👻😹",
"مسطول أتجوز صينية قالتله مالك ساكت ليه؟ قالها مش عارف افتكرتك نايمة 👻😹",
"واحدة صعيدية جوزها رماها من الدور الثالث طلعتله وقالتله بلاش الهزار البايخ ده 👻😹",
"اتنين مساطيل حبوا يسرقوا عمارة فقالوا لبعض إحنا ناخد العمارة بعيد ونسرقها برحتنا 👻😹",
"منهم بص ورا ملقاش الهدوم فقال له كفاية كدة احنا بعدنا أوى 👻😹",
"حر جدًا، قالتله مفيش مشكلة نطلعها بالليل 👻😹",
"واحد رجع في كلامه خبط اللي وراه 👻😹",
"واحد خلقه ضاق أعطاه لأخوه الصغير 👻😹",
"مرة مدرس رياضيات خلف ولدين واستنتج التالت 👻😹",
"واحد كهربائي أتجوز أربعة جابلهم مشترك 👻😹",
"كفايه عليك كده ياد يبن الحلوهه 👻😹",
"واحدة اسمها ساندي دخلت هندسة بقت ساندي متر مربع 👻😹",
"مرة شرطي مرور خلّف ولد بيتكلم بالإشارة 👻😹",
"مره واحد اسمو جابوا  كان بيرجم ابليس ف الحج قالولو ليه؟ قال عشان يمكن احتاجو 👻😹",
"ﻣﺮه واﺣﺪ ﻣﺴﻄﻮل ﻣﺎﺷﻰ ﻓﻰ اﻟﺸﺎرع ﻟﻘﻰ مذﻳﻌﻪ ﺑﺘﻘﻮﻟﻪ ﻟﻮ ﺳﻤﺤﺖ ﻓﻴﻦ اﻟﻘﻤﺮ ﻗﺎﻟﻬﺎ اﻫﻮه ﻗﺎﻟﺘﻠﻮ ﻣﺒﺮوك ﻛﺴﺒﺖ ﻋﺸﺮﻳﻦ ﺟﻨﻴﻪ ﻗﺎﻟﻬﺎ ﻓﻰ واﺣﺪ ﺗﺎﻧﻰ ﻫﻨﺎك اﻫﻮه  👻😹",
"واحد بيشتكي لصاحبه بيقوله أنا مافيش حد بيحبني ولا يفتكرني أبدًا، ومش عارف أعمل إيه قاله سهلة استلف من الناس فلوس هيسألوا عليك كل يوم 👻😹",
" مرة واحد مصري دخل سوبر ماركت في الكويت عشان يشتري ولاعة راح عشان يحاسب بيقوله الولاعة ديه بكام قاله دينار قاله منا عارف ان هي نار بس بكام 👻😹",
"بنت حبت تشتغل مع رئيس عصابة شغلها في غسيل الأموال 👻😹",
"واحد بيشتكي لصاحبه بيقوله أنا مافيش حد بيحبني ولا يفتكرني أبدًا، ومش عارف أعمل إيه قاله سهلة استلف من الناس فلوس هيسألوا عليك كل يوم 👻😹",
"ﻣﺮه واﺣﺪ ﻣﺴﻄﻮل ﻣﺎﺷﻰ ﻓﻰ اﻟﺸﺎرع ﻟﻘﻰ مذﻳﻌﻪ ﺑﺘﻘﻮﻟﻪ ﻟﻮ ﺳﻤﺤﺖ ﻓﻴﻦ اﻟﻘﻤﺮ؟ ﻗﺎﻟﻬﺎ اﻫﻮه ﻗﺎﻟﺘﻠﻮ ﻣﺒﺮوك ﻛﺴﺒﺖ ﻋﺸﺮﻳﻦ ﺟﻨﻴﻪ ﻗﺎﻟﻬﺎ ﻓﻰ واﺣﺪ ﺗﺎﻧﻰ ﻫﻨﺎك اﻫﻮه 👻😹",
"واحده ست سايقه على الجي بي اي قالها انحرفي قليلًا قلعت الطرحة 👻😹",
"مرة واحد غبي معاه عربية قديمة جدًا وبيحاول يبيعها وماحدش راضي يشتريها.. راح لصاحبه حكاله المشكلة صاحبه قاله عندي لك فكرة جهنمية هاتخليها تتباع الصبح أنت تجيب علامة مرسيدس وتحطها عليها. بعد أسبوعين صاحبه شافه صدفة قاله بعت العربية ولا لاء؟ قاله انت  مجنون حد يبيع مرسيدس 👻😹",
"مره واحد بلديتنا كان بيدق مسمار فى الحائط فالمسمار وقع منه فقال له :تعالى ف مجاش, فقال له: تعالي ف مجاش. فراح بلديتنا رامي على المسمار شوية مسمامير وقال: هاتوه 👻😹",
"واحدة عملت حساب وهمي ودخلت تكلم جوزها منه ومبسوطة أوي وبتضحك سألوها بتضحكي على إيه قالت لهم أول مرة يقول لي كلام حلو من ساعة ما اتجوزنا 👻😹",
"بنت حبت تشتغل مع رئيس عصابة شغلها في غسيل الأموال 👻😹",
"مره واحد اشترى فراخ علشان يربيها فى قفص صدره 👻😹",
"مرة واحد من الفيوم مات اهله صوصوا عليه 👻😹",
"ﻣﺮه واﺣﺪ ﻣﺴﻄﻮل ﻣﺎﺷﻰ ﻓﻰ اﻟﺸﺎرع ﻟﻘﻰ مذﻳﻌﻪ ﺑﺘﻘﻮﻟﻪ ﻟﻮ ﺳﻤﺤﺖ ﻓﻴﻦ اﻟﻘﻤﺮ ﻗﺎﻟﻬﺎ اﻫﻮه ﻗﺎﻟﺘﻠﻮ ﻣﺒﺮوك ﻛﺴﺒﺖ ﻋﺸﺮﻳﻦ ﺟﻨﻴﻪ ﻗﺎﻟﻬﺎ ﻓﻰ واﺣﺪ ﺗﺎﻧﻰ ﻫﻨﺎك اﻫﻮه 👻😹",
"مره واحد شاط كرة فى المقص اتخرمت. 👻😹",
"مرة واحد رايح لواحد صاحبهفا البواب وقفه بيقول له انت طالع لمين قاله طالع أسمر شوية لبابايا قاله يا أستاذ طالع لمين في العماره 👻😹",
" وهه عاوز تانيي 👻😹 "]
    bar = random.choice(selections)
    await message.reply_text(bar)
