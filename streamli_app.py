import streamlit as st

# Title of the app with right-to-left text alignment
st.markdown("<h1 style='text-align: right;'>دراسة تحليلية لاتخاذ القرار الأمثل للسكن: شراء أم إيجار؟</h1>", unsafe_allow_html=True)

# Introduction section
st.markdown("""
    <div style='text-align: right;'>
    يوسف، مهندس ذو خبرة خمس سنوات، يعمل حاليًا في مدينة تبوك. وقد حصل مؤخرًا على قبول للعمل في شركة أرامكو، 
    التي يقع مقرها شمال الرياض في حي العقيق. مع راتب يصل إلى 35 ألف ريال شهريًا، يواجه يوسف قرارًا مهمًا يتعلق 
    باختيار السكن المناسب له ولعائلته المكونة من زوجته وابنه الوحيد.

    نظرًا لأن الرياض مدينة كبيرة ومعروفة بازدحامها المروري، فإن القرب من مقر العمل يُعد أولوية قصوى لتوفير الوقت 
    والجهد. علاوة على ذلك، يبحث يوسف عن سكن يوفر له ولأسرته الراحة والاستقرار، ويكون قريبًا من الخدمات الأساسية مثل 
    المدارس، المرافق الصحية، والمجمعات التجارية.

    **تركز هذه الدراسة التحليلية على الخيارات المتاحة أمام يوسف بين شراء أرض، شراء منزل، أو شراء شقة.**
    وسوف يتم تحليل كل خيار بناءً على مجموعة من العوامل الرئيسية التي تشمل:

    <ul style="list-style-position: inside; text-align: right; direction: rtl;">
        <li><strong>القرب من العمل</strong>: لتقليل وقت التنقل اليومي.</li>
        <li><strong>التكلفة والميزانية</strong>: بما يتناسب مع راتبه الشهري وإمكانياته المالية.</li>
        <li><strong>توفر الخدمات</strong>: مثل المدارس، الأسواق، والمرافق العامة.</li>
        <li><strong>المرونة والاستقرار</strong>: مدى ملاءمة الخيار لاحتياجات أسرته الحالية والمستقبلية.</li>
    </ul>

    تهدف هذه الدراسة إلى مساعدة يوسف في اتخاذ قرار مستنير يتناسب مع ظروفه الشخصية والمهنية، ويحقق له التوازن بين الراحة، الاستقرار، والتكاليف.
    </div>
""", unsafe_allow_html=True)

# Option 1: Buying Land
st.markdown("<h2 style='text-align: right;'>خيار الأول: شراء أرض</h2>", unsafe_allow_html=True)
st.markdown("""
    <div style='text-align: right;'>
    في ظل ظروف يوسف الحالية، شراء الأرض ثم بناء المنزل ليس الخيار الأمثل، نظرًا لضيق الوقت والتكاليف المرتبطة بالبناء.
    يمكن اعتبار شراء الأرض كخيار استثماري مستقبلي إذا كان يوسف يبحث عن استثمار طويل الأجل، ولكن في الوقت الحالي، من الأفضل 
    التركيز على خيارات سكن جاهزة مثل شراء منزل أو شقة، أو استئجار فيلا قريبة من العمل.
    </div>
""", unsafe_allow_html=True)

# Option 2: Buying a Ready Villa
st.markdown("<h2 style='text-align: right;'>خيار الثاني: شراء فيلا جاهزة</h2>", unsafe_allow_html=True)
st.markdown("""
    <div style='text-align: right;'>
    في حال اتخاذ قرار شراء فيلا، يجب مراعاة أن العائلة قد تكبر في المستقبل، وأن الفيلا ستكون بيت العمر.
    بناءً على ذلك، يبحث يوسف عن فيلا بالمواصفات التالية:

    <ul style="list-style-position: inside; text-align: right; direction: rtl;">
        <li><strong>عدد الغرف</strong>: ٥ غرف.</li>
        <li><strong>المرافق</strong>:
            <ul style="list-style-position: inside; text-align: right; direction: rtl;">
                <li>حديقة</li>
                <li>٥ حمامات</li>
                <li>مطبخ مجهز</li>
                <li>صالتين</li>
                <li>مصعد</li>
                <li>غرفة للسائق</li>
                <li>غرفة خادمة</li>
            </ul>
        </li>
        <li><strong>الحالة</strong>: مؤثثة بالكامل.</li>
        <li><strong>عمر العقار</strong>: بين 0 إلى 3 سنوات.</li>
        <li><strong>المساحة</strong>: بين 300 إلى 500 متر مربع.</li>
    </ul>
    </div>
""", unsafe_allow_html=True)

st.markdown("١) يعرض الرسمة التالية متوسط أسعار الأراضي الفلل في كل منطقة من مدينة الرياض", unsafe_allow_html=True)
st.markdown("٢) فيما يلي متوسط أسعار الفلل في أحياء شمال الرياض التي تتوافق مع هذه المواصفات", unsafe_allow_html=True)

# Option 3: Renting an Apartment
st.markdown("<h2 style='text-align: right;'>خيار الثالث: استئجار شقة</h2>", unsafe_allow_html=True)
st.markdown("""
    <div style='text-align: right;'>
    في حال لم تسمح الميزانية بشراء فيلا، سيكون الخيار هو استئجار شقة. ومع ذلك، ستكون المواصفات التي يبحث عنها أقل، 
    حتى يتمكن من توفير المال لشراء منزل في المستقبل. المواصفات المطلوبة للشقة كالتالي:

    <ul style="list-style-position: inside; text-align: right; direction: rtl;">
        <li><strong>عدد الغرف</strong>: 3 غرف نوم.</li>
        <li><strong>المرافق</strong>:
            <ul style="list-style-position: inside; text-align: right; direction: rtl;">
                <li>حديقة</li>
                <li>3 حمامات</li>
                <li>مطبخ مجهز بالكامل</li>
            </ul>
        </li>
        <li><strong>الحالة</strong>: مؤثثة بالكامل.</li>
        <li><strong>عمر العقار</strong>: يتراوح بين 0 إلى 3 سنوات.</li>
        <li><strong>المساحة</strong>: 140 متر مربع</li>
    </ul>
    </div>
""", unsafe_allow_html=True)

st.markdown("٣) يعرض الرسمة التالية متوسط أسعار الأراضي الشقق في كل منطقة من مدينة الرياض", unsafe_allow_html=True)
st.markdown("٤) فيما يلي نظرة على متوسط أسعار إيجار الشقق في أحياء شمال الرياض التي تتماشى مع المواصفات المطلوبة", unsafe_allow_html=True)

st.markdown("""
    <div style='text-align: right;'>
    بعد عرض كافة الخيارات، يمكننا الآن التفكير في الفارق بين كل خيار، وما هو الخيار الأفضل بناءً على الميزانية، 
    الموقع، والخدمات المتاحة في كل منطقة. الهدف هو مساعدته في اتخاذ قرار مناسب يناسب حياته العملية والعائلية.
    </div>
""", unsafe_allow_html=True)
