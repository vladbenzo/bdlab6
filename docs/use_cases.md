# Розроблення функціональних вимог до системи

## Модель прецедентів

### Загальна діаграмм прецедентів

Рисунок 1 ілюструє загальну схему прецедентів та визначає ключові взаємодії.

<center>

![Діаграма](//www.plantuml.com/plantuml/png/RLD1QnD15BxFhnZIWwSeL1gBXz8sRK-Ub7eIP4o6TTbafyniA465jh5wAKHAQC6BYFw0PKrmcwRrBypy8x_PsGcZRI2xEs--zxxlVMzcKsLCPeD-ZwWaJW-OP7tAEfcGBx9XZrDso9Neys1pe7Y7AKxV4OhVDkiaaHI3jDiMFI7fojxENcltiTiJiijb7LzRR-q-MQlYMrAAmpgysbhVtbab7mYfIEdBMCNspHHjw7DpeQUwi4ypqeNEpUS6NOaa6zRevppQLxn6NsB_IC_Cn1oR4tFqy5Mgl-fRX4eR20gePFYcD-1rZQrkFqvT1S3rZJdHC_jiwXpa2v3V82TvovAOa0Eqoo8ExCHSc4kgVu71LZz3Qe4_rXHfjpNb7pDgEAUMlkstNqEs8_mEii9fn5T9GJc7o97bR_oVzKn4NkYFofGhbrDGS-nwXF052E5c8FIdBQVdvfCJ_FjVbohPEG2bERr7QLka6Kypn_eDQKX5ZzTchAVq4TNdkeJYfScs4hIFOVq2m2b4vaq00bllwFlYNMwQZw7KUzI4ex9Qx4m3oldTQMDteSkAqP-iPdF3p-0f3Qqm8tnXabYDG_JIU-3X-ocwcO85I4By0GGijCi2AwSde0SS_Km8gUHxg5i0k3nb07aT03-Wc39AmEqSVf-Xovdhb5PJkyRoAk1_l-7lZkS9GviyxUAE_mK0)

</center>
Рисунок 1: Загальна схема прецедентів

Специфікація прецедентів використання
Загальна схема прецедентів

Відповідно до схеми, система розрізняє 3 ролі акторів:

Відвідувач - неаутентифікований користувач. Може створити новий акаунт або увійти в існуючий.
Зареєстрований користувач - аутентифікований користувач. Має доступ до функцій роботи з медіа-контентом.
Адміністратор контенту - аутентифікований користувач з розширеними повноваженнями. Має доступ до управління іншими обліковими записами.

Рисунок 2 деталізує доступні дії для неаутентифікованого відвідувача.

<center>

![Діаграма](//www.plantuml.com/plantuml/png/LP3DIiGm58NtUOhBxESLPC2jAq5NWeIPC1IqXQRTsyQVPQL8r_e6fRPGYkapdFj6tgW1PnF8pNVEbsHd2vqNvVsTqliYosc3bZkC6CBA3WDwVjcGjdITs4G8fKfhzjeQGTynyHjNNFE3OC_SSNEJueDh35XbDi73SqFmMCC8drW9FHQX7Rpat4_rrVdjfJd-AsxvAVW9emIumXmacF25MGIlxC8k5CZ9ev1Br1EMOFuDnEkZZvQBx9YaIlqzXRQ7xLcKdyuYkZFfGJxd6m00)

Рисунок 2: Схема можливостей Відвідувача
</center>



<center>
Схема прецедентів для Зареєстрованого користувача







![Діаграма](//www.plantuml.com/plantuml/png/XPHHQzDG5CVVyoakzK5zADXIHMMKQSKFiDatGMxJaxOqIyPDYg88syhGjy4e3dnGmIyGv-fgJViPplr6_kzD5cjafg7jlUVyStxdVtB9TXHB5K_sV2SQZu9zgUIUw4btF53X9EXtGZzKueRtm5mRYab4hen8l744Fe_BUcfuTpmlouMgJogFj-xTR_PQDlv8gV1b7cvwBLms_3GCujtHQnADLh7FL3qVb8sIpuOZTnnG58c6ZUvaV1MG4isxpbl7aMwC-sfynea-uBcUwKDzXDMQppdX5I_uf-0bhn5QsDJK9FIxcf2HsA51Do8qvuy6mxZdJyXn5Bcn30O-eUX7b5df8vwRtxe-p4fWct9Io-UIJmdgBr1_upK4YU1BK3VlnZfz7jpYKxu4ViOf0XVwWpwnqXGYx3Yf6nE0JFK1S0aIYzksrMxdHGTZeY1sIjYPgGIfzGlKIOcifuPxTgKmxV4Ff7BjoemAt--ytkp3UBc9FfT6_wS5HJAcKWEVuVazvhgy1ho2uMFRP86zXeJzUS7Q9QdSOOdrAU_t5y__QpP5AN0jnpg-o4w3FgussTtl_slob1UcHWNugtbqoEUQQjOJyWai7EIhirYlj_zwsCNKIndnK6njqIii-r6xxHG3gvHbzYfbfhCgsJR-yLRv3G00)

Рисунок 3 показує функціонал, доступний зареєстрованому користувачеві.


</center>

Схема прецедентів для Адміністратора контенту

Рисунок 4 відображає спеціальні можливості адміністратора контенту.

<div style="text-align: center; margin: auto;">


<center>

![Діаграма](//www.plantuml.com/plantuml/png/dLDDQnH14BtthoXsBte8x4gY8c59L3oB7pSldPcQpR2ptT8zI_n0YBkW7WGzoEOYUCWV66E2IvAT_8NgVsHrTrZ62KHm1gRfLw_UUrtqRDbIcd8oBeGTvUgbD78CEp8P3OsUgFI1BhI1RfPbQNQdmPXOJAH5U2k0d_jN-9ZTJk_6cZOfcaiyaNAzrmlujZ5wxnBUaFuDy2EjogVv6uJ--ceVMJi5kpGad-tcoKYXjT0Fw9FeRnGQkBKXtWaXavBxElILZkdSpMdfvkwzcxfzgjoKQhSFT4ermrCwyLytwu2qi9sESmNT8X_kbg-nAFIU40QJKgfXWIptdNkEtOpEt6UWggtDXID6buny2VfijmYbK70VcNpKYODRZP4p_fVE2tM33kd2duZ1CuOYdnF-35lkuyA2pca1z9jP5rw4LmPkXjC-jsZ2YKKhqI6RpLZlv9eCLFa4tvXJqIcFSH7W3sv-DKDDlwXkP72pwFyG2opHfu0kzhDUbhLo7CIvK0NiNdl5QwByy32RB3sqYXxc-ebx3bOQqVonqMFTSkUB4s_0sjgWEPr6qBygS0ysD_5LYIgrWu68al_cRV7AVzqV)

Рисунок 4: Схема можливостей Адміністратора контенту
</center>


Сценарії взаємодії для Відвідувача
Реєстрація нового користувача (UserRegister)

Ідентифікатор: UserRegister

Назва: Процес реєстрації нового користувача

Актори: Відвідувач, Система

Передумови: Відвідувач системи не має існуючого облікового запису.

Результат: Створено новий обліковий запис користувача, готовий до використання.

Нештатні ситуації

Надані дані не відповідають очікуваному формату або правилам – InvalidDataException
Не всі обов'язкові поля реєстраційної форми заповнені – DataMissingException
Обліковий запис з вказаною електронною поштою вже існує – AlreadyRegisteredException

Основний потік подій

Відвідувач ініціює процес реєстрації (наприклад, натискає кнопку 'Реєстрація').
Відвідувач заповнює реєстраційну форму (вводить ім'я, прізвище, email, пароль).
Система приймає дані для реєстрації.
Система валідує отриману інформацію.
Система перевіряє, чи не існує вже акаунт з таким email.
Система створює новий запис про користувача в базі даних.
Система сповіщає користувача про успішне завершення реєстрації.

<center>

![Діаграма](//www.plantuml.com/plantuml/png/dLHDRzD04BtxLwp4WQJg0IHEyO4MA187EC2Lon9lmggE7TdRGY58AO424Y9I5QKdg2h-W8bYsdoa-Gkp_uWtQqj1wiUX6oNopiwyUU_jn1kfaOdPQOLUkgsZjanaIxoIzUrc4kz4mSCuZ1Dngw7uyr-6h1kzgysUUEy9h0SN2jmgpk8aK4aPl-EMYsycIVoc3DzpouKVnv5veTyfSNUrVoPR2lbQXju7p-lGeHtIc4RyQtiqein-wNXEXrUZ0rhOeJt0zuST2Dkbt0xills8fwm8-yWweeoMT8xYHP7tYSwHCRUzbr45mFFRjhykQ6cxs9mYxSn-etnTg9RK8Hy0h8lwcVrUzPdJ2JBGXNAQKzP1Xr-kvHb30Xyd6LVbJ8Yf0xYFE7HaJ1WOkY4gD2YsWgRWmwbJL29mlohCQnM92WFHj0flQdI8nncxK2hhCs5cDK4efmLblgV2L04N44NDCOjc6Wp41DY5ENZEQChYrvv4kpBKmIDfvDRRkceR7KThFcfJ4xSz5GMwKNBz3S730c36lKzNdb9-9MbKqH9alzBYWYKqHGW8VnW5Dm18-E3S_rmsWjpH3LIndASwJNNKl5xL5b-mi3t6PZfymxG0qkHIDSVExx5h_vTLewv_sTGTtO3qPfWe6UmzLqsT6fMeu6hgDJe1oeY7XkUvC97DAlsZINa_FAO-qdzYCxRxtAripeF46Co8nYir_ZL_EH3O00D-VVm3)

</center>

Аутентифікація користувача (UserLogin)

Ідентифікатор: UserLogin

Назва: Вхід користувача до системи

Актори: Відвідувач (що має акаунт), Система

Передумови: Користувач вже має зареєстрований обліковий запис.

Результат: Користувач успішно аутентифікований та отримує доступ до функцій системи для зареєстрованих користувачів.

Нештатні ситуації
Вичерпано ліміт невдалих спроб входу – TooManyActionsException
Надано невірний пароль або email – DataNotFoundException
Обліковий запис з таким email не знайдено – NotRegisteredException

Основний потік подій
Користувач відкриває форму автентифікації.
Користувач вводить свої облікові дані (email та пароль).
Система приймає запит на вхід.
Система верифікує надані облікові дані.
Система перевіряє існування акаунту з вказаним email.
Система авторизує користувача, надаючи доступ до захищених ресурсів.
Система інформує користувача про успішний вхід.

<center>

![Діаграма](//www.plantuml.com/plantuml/png/dLDDQnD16BxFhtZ1IzkJWgVcOEj7R_QW7hsCoQGktUo4tQbQZT3kLaG8HAJiGL3n7wnXOoNDnrzuvn_vl9D8X1gGJYwPTvwFvs5cTpAdKtVKYLLs62LTdUeEFTFDmuFK7YMjUpQsATre6_dzXT1D5xs8t36zKOHrzmeXhCMPJLicNSvlXXNcksbgNox7jyCAupsRkCVHQqEtLljztJ70HpfMRvNgyMUU-HF-vKzzxWiUSkNVzrJeeRRvao-vvh40mj4v-RE0d_Y2UEZVyOnhNpG42W0sKCfzdqn7Hp7vd2lYEOWdEBlq_OOuVb-uyOWdNFL0_GeA74GK3dp15JZG8Pw2BpOI0zoeJHlyZKT0ZtW8o0SU0JCZQ9UWb-3uKvu7knztDiazDmbjI0mURogYRR1dO491Xk8sns02yqlKB9ucMq-iVQYJurrSYaso1w-QfYl_jXgWPyvsbKbQKLk5nf11Y3DuZqDqSGrHnkBYI-8QpbDV_ib-ljYI0AG4UBaCraGDHKK8SGUYFqNc0VA34YwiJmB7iC0ebuimSMPW1C1_zhsldTwtRayUtFgs8Vt7bHL90Fn1wtzb1tI8RNXPV24eLBxwqBXg1FGN46le8TKof5mu149ohlcdt3Fi1gj7TvskwFd874IPCwbPNtRzHm783Z3oWVy6)

</center>
Сценарії взаємодії для Адміністратора контенту
Призначення іншої ролі користувачеві (UserRolePromote)

Ідентифікатор: UserRolePromote

Назва: Зміна ролі існуючого користувача

Актори: Адміністратор контенту, Система (можливо, сповіщення для Користувача)

Передумови:

Адміністратор контенту аутентифікований та має відповідні права.

Цільовий користувач має активний обліковий запис.

Результат: Роль цільового користувача успішно змінена.

Нештатні ситуації:

Поточний користувач не має прав адміністратора – RoleNotEnoughRightsException

Цільовий користувач не знайдений в системі – NotRegisteredException

Спроба призначити роль, яку користувач вже має, або найвищу можливу роль – RoleAlreadyHighestException

Основний потік подій

Адміністратор контенту вибирає цільового користувача в інтерфейсі управління.

Адміністратор контенту обирає нову роль для цього користувача.

Система отримує команду на зміну ролі.

Система перевіряє повноваження адміністратора.

Система перевіряє існування цільового користувача.

Система перевіряє, чи можлива зміна на обрану роль.

Система оновлює роль користувача в базі даних.

Система повідомляє адміністратора (та, можливо, користувача) про успішну зміну ролі.
<center>

![Діаграма](//www.plantuml.com/plantuml/png/dLHDRn916BxlhvZ4YxrfuaaEjfeQJptWrSiA0qmAEsHsKAkOy97eXLXZcZqOhV4V84Ax5bZ_mZl_oEST5hk9QvDs26pcdUTzFcQ6tOrjQ6olqmxYGnLrGnDsnFEmTjWqkXVL7-csDk9MG_AdW0XhLhrGzaYy2GJ6mtyQ_DYiQLEN9g_VySFNzupHB_FoFJzy-R6Ex5FrMegxb_E3i2E1Ls4xU1i4VVf8SrgvXDOkSKCtSWEQkX5bRY3eWZ9QOxBWNpVk1pvUS9y-KKe_AFNO4yO1ZkcGKJH3yJrD1NYNxbZG-OQUKW5GXbfI0SLfaM2D-ioDju19XOrzzuoilg9fdrkyknHquroLLz0yHoiUqxzQc1Urlj42qmKa4ZTmnzpycnKtkg0uuuXeWzjf-NRm4wvKGzoc4qonn0k0JIW37Q_JxC6Ei2qP0OFs7MmvQxC4zBbXgxn2YYLTkF6pgAhRya3R_KZtcgsgQhPilF-g9hjMwQW2XjZgRY2Zkce4fKdO9WVc77a6zyubl8kiZEzFoagFw3BGv_BpE-SzfLyqzxkJtI0SWbLbKyLM6bc_LYomP7G6djGNsTcaz2hb4RumdFqMG32Ltl14zjf6XlMZ9pWF6Tihd9_cTsZfFe1gUt__jzze-Cetp0rPBbTt2GgZZIMQ5-zYQTph_cFXTXTs-QNq1m00)

</center>

Усунення користувача (UserDelete)

Ідентифікатор: UserDelete

Назва: Видалення облікового запису користувача

Актори: Адміністратор контенту, Система (можливо, сповіщення для Користувача)

Передумови: Адміністратор контенту аутентифікований та має права на видалення користувачів. Цільовий користувач існує.

Результат: Обліковий запис цільового користувача видалено (або деактивовано) з системи.

Нештатні ситуації:

Поточний користувач не має прав на видалення – PermissionDeniedException

Цільовий користувач не знайдений в системі – NotRegisteredException

Основний потік подій

Адміністратор контенту вибирає користувача для видалення.

Система отримує команду на видалення користувача.

Система перевіряє повноваження адміністратора.

Система перевіряє існування цільового користувача.

Система видаляє (або позначає як видалений) обліковий запис користувача.

Система сповіщає адміністратора (та, можливо, користувача) про успішне видалення.

<div style="text-align: center; margin: auto;">
<center>

![Діаграма](//www.plantuml.com/plantuml/png/hLHFQnD15B_FftZKIt8G0WM57gIDQKz5Ylq4w-viN9BinjaDMaH84z0AGYH8JgBquZcDIPicRV8LtdmZVw-Rib4NxQ4BsTsPURy_xpUpsOuJnoIjHbt5jI1iEiPfq0l7hLLDr0gzfr4zClHWhxBtQ7TphIBMhrewT3MzLOHhnvZeTLfRqRfvM3igrriwNNAJo9GZuscJ5fJhO9SbsWzylH-4-Z-hVvhH9V-nxqWD7S1wu0PD9qpoITOA_iNpB4h-rl5zVzFrilLCGDPSjrHIxvHof3_QuCyyvYixu6ixiCUsOziyj1rUs3RnZ1UOxl14xhQxGKvCEruZ25KpimUAKvu2AdLNF9GgEZoA4zrGwgQQ7Zv9ORH5tESfdw5UPBw819G4BW8ymkG77X8ipMsFC9xYTSXpiG0JlJN6L48elm4B3dJHNL6A3m36jaju3FE8KlZlHDzv0g89Zn15s_Q4R0co4I2u0tv-2oSCycF3KuL8dKnGVPb8u0uknLz1SGxzgH315QHE012GEBJ7F9K8CF4UZBqjnNsmGqEaLxuN90sDePB6jRG3AWYLz7lZLkHvL5I50sqQGHm7KLZHOQ2ztJUkRYOO5fKEFHA7Tun0-kFhT7DMpOj5RD0diORVJrxaR-Hz9V4ZamFgCbUCX8ZuGZZuaiSIc1Ih0hw1vxeQe4DpznpwjmT6Cg02tiwaIz3YTGQhS2_7hKYymD8S3cUPlmiKBSLVnfrz0QVfeK9l7xDTawr5vqlCdaWdUKTs6uxnV_SB)

</center>
Сценарії взаємодії для Зареєстрованого користувача
Додавання медіа-контенту (ContentCreate)

Ідентифікатор: ContentCreate

Назва: Створення нового об'єкта медіа-контенту

Актори: Зареєстрований користувач, Система

Передумови: Користувач аутентифікований і володіє необхідними дозволами для створення контенту.

Результат: Новий медіа-об'єкт успішно додано до сховища системи.

Нештатні ситуації

Користувач не має дозволу на створення контенту – PermissionDeniedException

Спроба створити контент з ідентифікатором, що вже використовується – ContentIdExistsException

Надані дані контенту не пройшли перевірку (невірний формат, відсутні обов'язкові поля) – InvalidContentDataException

Основний потік подій

Користувач активує функцію створення контенту.

Система відображає форму для введення даних нового контенту.

Користувач заповнює форму та/або завантажує файли.

Система перевіряє права користувача на додавання контенту.

Система перевіряє унікальність ідентифікатора контенту (якщо застосовно).

Система валідує надані дані та файли.

Система зберігає новий медіа-об'єкт.

Система інформує користувача про успішне створення.

<div style="text-align: center; margin: auto;">
<center>

![Діаграма](//www.plantuml.com/plantuml/png/hLNVJXDF5BwVfvZmk-5tOTGBbN1X46eC2I4an0SOjrESqExMsG4XneG_1haWO0Y1n6YCRx1KYwNGyWfdtiXlpiAos6guO3TDftE-yttdctDsEv4wPTrIeoxIHHCtbLKD-Kf5YmisMOghKqaziVA_sgDmbn2fVhEauqZBTqBYUcPjyZR7LfHTdAyhfrzOjPe78vVOoSHMjSqXisevZyoOcfuniIu7AwPHP1RnF-lHZsjFQZN6pA5w4vccYbsPPhAEd070W2--63QRE3qiFgOV5l6o069HDFQ0OvF9oc2g2dSHBcNEc_gojkAz42gSZ1oX8yhy6hNzWL_t6rZrgKKPzQX3fvAwrCTMXqER8U0_ZaYLofSfI9hNvi3pFOTHcyufOz3yQkfqGuW0blUUSf8Sb_I9ki1rgEKt_O7q7y3SmzQMF_IxaZbQBDl6Ti_lSHLO1EfUgACWp0K29KpG1GhO01tddbDd29N8Csxcxlj3-Wc5O-0oEe77WuB5Rqh4pb348DbVoy098hvxa-Q-f5-8yjc22KANxh4yfJFg3Atj6xLPi8MpMVDxIA0BR33FqEvG9c8CYxHcuRKBSw9m2Vg2eaw2IfxO0-rsg0AV7cKmHntcoBWBU-E2la8LfyAs6UPtg5-e_-DKHkUqRPWqDKbSqR7HrUShaMuw_FnVwBWgGtctz1e60ytfGl4CybYprHqvNRaZbv_BauKEIMvD5mpd497K0bzR1bq0q2ynEfN4JiTk6hPCwjBRcjjd3nWqxdee1oUO1KloQd67ZSi70z-0bIK67wNHwNXPrKtrqbP5ENLRIqTq73e6KpyWpwOm-VpUk2bpdLsy0hQmNpmRLrFTbrYlOtdejuFJOTCrWPBmV_4R)

</center>
Пошук медіа-контенту (ContentSearch)

Ідентифікатор: ContentSearch

Назва: Пошук існуючого медіа-контенту

Актори: Зареєстрований користувач, Система

Передумови: Користувач аутентифікований в системі.

Результат: Система надає користувачеві список медіа-об'єктів, що відповідають критеріям пошуку.

Нештатні ситуації:

Пошук за ідентифікатором, якого не існує в системі – InvalidContentIdException

Введені некоректні або несумісні параметри для пошуку/фільтрації – InvalidSearchRequestException

Основний потік подій:

Користувач ініціює дію пошуку контенту.

Система надає інтерфейс для введення пошукових критеріїв та фільтрів.

Користувач вводить пошуковий запит та/або застосовує фільтри.

Система перевіряє валідність введених критеріїв.

Система виконує пошук у сховищі контенту за заданими параметрами.

Система формує список знайдених результатів.

Система відображає результати пошуку користувачеві.
<div style="text-align: center; margin: auto;">
<center>

![Діаграма](//www.plantuml.com/plantuml/png/hLFB3j905DtFLqpY1bRkwOP4NR3LBsYW20cs28DnmO82GHT44q9AOdHXuWTKqafvjFp2lN_akHrZ8CY6ID8mcJcFSswdzQ5n1sRqfgVKc3OKyuHINdF8KwmAsb9CEMMqrtIW0bjPUJIJ0_umLYLRrJGjAEU85tW-yLfJ8WjDPt0-0dtWcIC6tosVKZfHF1RUDnWa58F34IHmn1EU0x3dy8R_G41OhB0kO99XVmcOWAmHGcxqKqqxOC42FnH9dacSEG8TUGaIy7VIh-1-12uHoaLSKR6X88rj-3dA3uod1ztN7QEVjDikVeg-0lcBZi0YhqQJ509JYl7as42UJDfWGqRxkQOmiDGsbN-1SIJ6CfSOkLARzsfqgjBmtxczRkkLvmwQdPVUsv4tD2_UDxs-wGP-LNb-IqiwMoaJVUXULz9_TgL-Bfd-Io5TeVDDtd9gkl6yYhfVBarne4MC3j0_0L4Q21pQjAT4O5JyxViiy8tdcqRhJjSVvHnFzds7yfxa0g1hETqTqk02sFGSqTOfvuDL0j1F6JYgojMzXLFsp_i8s9OZvz5lBUWhLKS1-Ln_0m00)

</center>
Зміна інформації про медіа-контент (ContentUpdate)

Ідентифікатор: ContentUpdate

Назва: Редагування метаданих існуючого медіа-контенту

Актори: Зареєстрований користувач, Система

Передумови: Користувач аутентифікований та має права на редагування конкретного об'єкта контенту.

Результат: Інформація про вказаний медіа-об'єкт оновлена в системі.

Нештатні ситуації:

Спроба редагувати контент за ідентифікатором, якого не існує – InvalidContentIdException

Користувач не має дозволу на редагування цього контенту – PermissionDeniedException

Оновлені дані не пройшли валідацію – InvalidContentDataException

Основний потік подій:

Користувач обирає функцію редагування для певного медіа-об'єкта.

Система надає форму з поточними даними контенту для редагування.

Користувач вносить зміни в поля форми.

Система перевіряє існування контенту, що редагується.

Система перевіряє права користувача на редагування цього контенту.

Система валідує змінені дані.

Система оновлює інформацію про медіа-об'єкт у сховищі.

Система повідомляє користувача про успішне оновлення.

<div style="text-align: center; margin: auto;">

Зміна інформації про медіа-контент (ContentUpdate)

Ідентифікатор: ContentUpdate

Назва: Редагування метаданих існуючого медіа-контенту

Актори: Зареєстрований користувач, Система

Передумови: Користувач аутентифікований та має права на редагування конкретного об'єкта контенту.

Результат: Інформація про вказаний медіа-об'єкт оновлена в системі.

Нештатні ситуації:

Спроба редагувати контент за ідентифікатором, якого не існує – InvalidContentIdException

Користувач не має дозволу на редагування цього контенту – PermissionDeniedException

Оновлені дані не пройшли валідацію – InvalidContentDataException

Основний потік подій:

Користувач обирає функцію редагування для певного медіа-об'єкта.

Система надає форму з поточними даними контенту для редагування.

Користувач вносить зміни в поля форми.

Система перевіряє існування контенту, що редагується.

Система перевіряє права користувача на редагування цього контенту.

Система валідує змінені дані.

Система оновлює інформацію про медіа-об'єкт у сховищі.

Система повідомляє користувача про успішне оновлення.

<div style="text-align: center; margin: auto;">
<center>

![Діаграма](//www.plantuml.com/plantuml/png/hPJ1gjD058RtynG3RgwlSE_cWdNHdQyGRAu6xaqkxIWkkcXIq2vA0wL446tn3MAjsZQPz1NEUIF_Cp5IIeCWxIR3pFd_-VuvCxqT6AzltZpSApMaZvJpY7xmWcDECAfeJJbPsj9EqvugJ6tTqbWM-CDGERMwrhIaRrWRONQXeJlmUyvufiMEDZ3v3arjPZbrPXWaMBHYToCMSzeUcxWIsZkWf8OuqVrHMO35q2KyrVIBIiwaMjDQkvqjPpSIxclD3cb9-L2aApWBtnge8qwnAGOnsN-WXf7nTJzuzThe9tTt7dwAFgFe9nM0X5AJXVC4cjoHvxhcWs_kpYMzLlJfs1RSMiff3uTITplE0hEYfXroe8mgTTKDtthtGUzP51e_DDtUytSl_KSJHE5JvOSzBMZdaz51phMXoriQSwbmNvmvsjAKyPIgXi7rfU2qXK5TlV3x3y5WW5GTFmpyjf1pA0eqUyFZ-j9PTs4BTwJPKVClbwb-0_YwJ5dxfgUTwdZ6QucnR2nuXXYDmVadif9AYOnl2SNVpbOQXn1ZcF54mfoGkTx-xmkF7fMw1R7yIVm6)

</center>
</div>