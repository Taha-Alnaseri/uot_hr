<p><!DOCTYPE html></p>

<html dir="rtl" lang="ar">
<head>
    <meta charset="UTF-8">
    <style>
        body {
            font-family: 'Segoe UI', Tahoma, Arial, sans-serif;
            direction: rtl;
            text-align: right;
            background-color: #f4f4f4;
            margin: 0;
            padding: 20px;
        }
        .container {
            max-width: 600px;
            margin: 0 auto;
            background-color: #ffffff;
            border-radius: 10px;
            box-shadow: 0 2px 10px rgba(0,0,0,0.1);
            overflow: hidden;
        }
        .header {
            background-color: #1a73e8;
            color: white;
            padding: 30px;
            text-align: center;
        }
        .header h1 {
            margin: 0;
            font-size: 22px;
        }
        .header p {
            margin: 5px 0 0 0;
            font-size: 14px;
            opacity: 0.9;
        }
        .body {
            padding: 30px;
        }
        .greeting {
            font-size: 16px;
            color: #333;
            margin-bottom: 20px;
        }
        .info-table {
            width: 100%;
            border-collapse: collapse;
            margin: 20px 0;
        }
        .info-table tr {
            border-bottom: 1px solid #f0f0f0;
        }
        .info-table tr:last-child {
            border-bottom: none;
        }
        .info-table td {
            padding: 12px 10px;
            font-size: 14px;
        }
        .info-table td:first-child {
            color: #888;
            width: 40%;
            font-weight: bold;
        }
        .info-table td:last-child {
            color: #333;
        }
        .status-badge {
            display: inline-block;
            background-color: #fff3cd;
            color: #856404;
            padding: 4px 12px;
            border-radius: 20px;
            font-size: 13px;
            font-weight: bold;
        }
        .notice {
            background-color: #e8f4fd;
            border-right: 4px solid #1a73e8;
            padding: 15px;
            border-radius: 5px;
            font-size: 14px;
            color: #555;
            margin: 20px 0;
        }
        .footer {
            background-color: #f8f8f8;
            padding: 20px 30px;
            text-align: center;
            font-size: 12px;
            color: #999;
            border-top: 1px solid #eee;
        }
    </style>
</head>
<body>
    {% set status_map = {
    'Pending': 'قيد الانتظار',
    'Approved': 'تم الموافق عليه',
    'Rejected': 'مرفوض',
    'approved by the line manager': 'تمت موافقة المدير المباشر',
    'Approved by the Administrative Associate': 'تمت موافقة المعاون الإداري'
    } %}

    <div class="container">

        <!-- Header -->
        <div class="header">
            <h1>الجامعة التكنولوجية - كلية الهندسة الميكانيكية</h1>
            <p>طلب أجازة</p>
        </div>

        <!-- Body -->
        <div class="body">

            <p class="greeting">
                السلام عليكم ورحمة الله وبركاته،<br>
                عزيزي <strong>{{ doc.data_lprk }}</strong>،
            </p>

            <p style="color: #555; font-size: 15px;">
                نود إعلامكم بأنه تم استلام طلب إجازتكم بنجاح، وهو الآن قيد المراجعة .
            </p>

            <!-- Details Table -->
            <table class="info-table">
                <tr>
                    <td>رقم الطلب</td>
                    <td><strong>{{ doc.name }}</strong></td>
                </tr>
                <tr>
                    <td>الرقم الوظيفي</td>
                    <td>{{ doc.employee }}</td>
                </tr>
                <tr>
                    <td>الاسم الكامل</td>
                    <td>{{ doc.data_lprk }}</td>
                </tr>
                <tr>
                    <td>نوع الإجازة</td>
                    {% set leave_type_name = frappe.db.get_value("UOT Leave Type", doc.leave_type, "leave_type") %}
                    <td>{{ leave_type_name }}</td>
                </tr>
                <tr>
                    <td>تاريخ تأريخ بدأ الاجازة</td>
                    <td>{{ doc.from_day }}</td>
                </tr>
                <tr>
                    <td>تاريخ تأريخ انتهاء الاجازة</td>
                    <td>{{ doc.to_day }}</td>
                </tr>
                <tr>
                    <td>عدد الأيام</td>
                    <td>{{ doc.days_count_of_leave }} يوم</td>
                </tr>
                {% set leave_type_name2 = frappe.db.get_value('UOT Leave Type', doc.leave_type, 'leave_type') %}
                {% if doc.leave_type == 'Leave Type- 003' %}
                <tr>
                    <td>سبب الإجازة</td>
                    <td>{{ leave_type_name2 }}</td>
                </tr>
                {% else %}
                <tr>
                    <td>سبب الإجازة</td>
                    <td>{{ doc.reason_for_leave }}</td>
                </tr>
                {% endif %}
                <tr>
                    <td>حالة الطلب</td>
                    <td>
                        <span class="status-badge">{{ status_map.get(doc.workflow_state, doc.workflow_state) }}</span>
                    </td>
                </tr>
            </table>

            <!-- Notice -->
            <div class="notice">
                سيتم إشعاركم عند اتخاذ القرار بشأن طلبكم. في حال وجود أي استفسار يرجى التواصل مع شعبة الموارد البشرية ,<strong>تعتبر هذه الرسالة طلب رسمي من قبلك و على وفق السياقات</strong>.
            </div>

        </div>

        <!-- Footer -->
        <div class="footer">
            <p>هذه رسالة آلية من نظام إدارة الموارد البشرية - الجامعة التكنولوجية - كلية الهندسة الميكانيكية</p>
            <p>يرجى عدم الرد على هذا البريد الإلكتروني</p>
        </div>

    </div>
</body>
</html>
