# -*- coding: utf-8 -*-
"""تنظیمات کلی پروژه."""

import os

# ⚠️ توکن ربات از BotFather روبیکا. برای امنیت، ترجیحاً از متغیر محیطی بخونیدش
# (مثلاً: RUBIKA_BOT_TOKEN=xxxxx python bot.py) تا مجبور نباشید توکن رو مستقیم
# داخل کد بنویسید و دستی هم به گیت‌هاب پابلیک پوش نشه.
BOT_TOKEN = os.environ.get("RUBIKA_BOT_TOKEN", "CFFEBE0IHUSMMEXJRKJYTOGMKMEGGBYLZWPRLBDYIUPRNCWYJXFGDUGACBYFSMPM")

DB_PATH = "support_bot.db"

# آیدی(های) اولیه‌ای که به عنوان OWNER (بالاترین دسترسی) ثبت می‌شن.
# همون sender_id ای که وقتی به بات پیام می‌دید در دیتابیس/لاگ می‌بینید.
INITIAL_OWNER_IDS = [
    "",
]

STALE_THRESHOLD_MINUTES = 30

# ---------------- سیستم رنک Staff ----------------
RANK_HELPER = "HELPER"
RANK_MOD = "MOD"
RANK_ADMIN = "ADMIN"
RANK_MANAGER = "MANAGER"
RANK_OWNER = "OWNER"

RANK_LEVEL = {
    RANK_HELPER: 1,
    RANK_MOD: 2,
    RANK_ADMIN: 3,
    RANK_MANAGER: 4,
    RANK_OWNER: 5,
}

RANK_LABELS_FA = {
    RANK_HELPER: "🧰 هلپر",
    RANK_MOD: "🛡️ ماد",
    RANK_ADMIN: "⚙️ ادمین",
    RANK_MANAGER: "📋 منیجر",
    RANK_OWNER: "👑 اونر",
}

PERMISSION = {
    "TICKET_BASIC": RANK_HELPER,
    "FAQ_CREATE": RANK_MOD,
    "SYSTEM_STATS": RANK_ADMIN,
    "BROADCAST": RANK_ADMIN,
    "STAFF_MANAGE": RANK_MANAGER,
}

# ---------------- وضعیت‌های تیکت ----------------
STATUS_NEW = "NEW"
STATUS_SEEN = "SEEN"
STATUS_WAITING_STAFF = "WAITING_STAFF"
STATUS_IN_PROGRESS = "IN_PROGRESS"
STATUS_WAITING_USER = "WAITING_USER"
STATUS_ANSWERED = "ANSWERED"
STATUS_CLOSED = "CLOSED"

ALL_STATUSES = (STATUS_NEW, STATUS_SEEN, STATUS_WAITING_STAFF, STATUS_IN_PROGRESS,
                 STATUS_WAITING_USER, STATUS_ANSWERED, STATUS_CLOSED)
OPEN_STATUSES = tuple(s for s in ALL_STATUSES if s != STATUS_CLOSED)

STATUS_LABELS_FA = {
    STATUS_NEW: "🆕 جدید",
    STATUS_SEEN: "👀 دیده‌شده",
    STATUS_WAITING_STAFF: "⏳ منتظر پاسخ پشتیبانی",
    STATUS_IN_PROGRESS: "💬 در حال پاسخ‌گویی",
    STATUS_WAITING_USER: "📨 منتظر پاسخ کاربر",
    STATUS_ANSWERED: "📨 پاسخ‌داده‌شده",
    STATUS_CLOSED: "🔒 بسته‌شده",
}
