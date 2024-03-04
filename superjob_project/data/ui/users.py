from dataclasses import dataclass


@dataclass
class Person:
    first_name: str
    last_name: str
    birth_date: str


@dataclass
class Employment:
    position: str
    salary: str
    experience: str
    company_title: str
    company_description: str
    work_description: str


@dataclass
class Time_work:
    month: str
    year: str
    month_end: str
    year_end: str


# Usage
person = Person(first_name='Johnatan', last_name='Doe', birth_date='01.01.1990')
employment = Employment(position='Assembler developer', salary='385000', experience='Automation QA',
                        company_title='QA.GURU', company_description='Образование',
                        work_description="Изучал автоматизацию тестов")
time_w = Time_work(month='Январь', year='2018', month_end='Декабрь', year_end='2020')
