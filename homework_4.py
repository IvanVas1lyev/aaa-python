"""
Service for get information about departments and their characteristics
"""

import csv


def read_corp_data(file_name: str) -> dict:
    """
    Read file with data about departments and structures it
    :param file_name: name of file with departments data
    :return: dict with structured info about departments
    """
    dep_data = {}

    with open(file_name, 'r', encoding='utf-8') as file:
        my_reader = csv.reader(file, delimiter=';')
        next(my_reader)

        for employee in my_reader:
            employee_data = {
                'name': employee[0],
                'division': str(employee[2]),
                'mark': float(employee[4]),
                'salary': int(employee[5])
            }

            if employee[1] in dep_data:
                dep_data[employee[1]]['max_sal'] = max(dep_data[employee[1]]['max_sal'], employee_data['salary'])
                dep_data[employee[1]]['min_sal'] = min(dep_data[employee[1]]['min_sal'], employee_data['salary'])
                dep_data[employee[1]]['uniq_divisions'].add(employee_data['division'])
                dep_data[employee[1]]['average_sal'] += employee_data['salary']
                dep_data[employee[1]]['employee_count'] += 1
            else:
                dep_data[employee[1]] = {
                    'max_sal': employee_data['salary'],
                    'min_sal': employee_data['salary'],
                    'average_sal': employee_data['salary'],
                    'uniq_divisions': {employee_data['division']},
                    'employee_count': 1
                }

        for dep in dep_data.values():
            dep['average_sal'] /= dep['employee_count']

    return dep_data


def get_hierarchy(dep_data: dict) -> None:
    """
    Print hierarchy for every department
    :param dep_data: dict with structured info about departments
    :return: None
    """
    for dep_name in dep_data:
        print(f'{dep_name}:')

        for div_name in dep_data[dep_name]['uniq_divisions']:
            print(f'● {div_name}')

        print()


def get_report(dep_data: dict) -> None:
    """
    Print report for every department
    :param dep_data: dict with structured info about departments
    :return: None
    """
    for dep_name, dep in dep_data.items():
        print(f'{dep_name}:')

        print(f'Средняя зарплата: {dep["average_sal"]}')
        print(f'Максимальная зарплата: {dep["max_sal"]}')
        print(f'Минимальная зарплата: {dep["min_sal"]}')
        print(f'Количество сотрудников: {dep["employee_count"]}')

        print()


def save_report_to_csv(dep_data: dict) -> None:
    """
    Save report for every department to report.csv file
    :param dep_data: dict with structured info about departments
    :return: None
    """
    dep_data_with_name_field = {}

    for dep_name, dep in dep_data.items():
        dep_data_with_name_field[dep_name] = {**{'dep_name': dep_name}, **dep}

    with open('report.csv', 'w', encoding='utf-8') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=dep_data_with_name_field[next(iter(dep_data_with_name_field))].keys())
        writer.writeheader()
        writer.writerows(dep_data_with_name_field.values())


if __name__ == '__main__':
    departments = read_corp_data('Corp_Summary.csv')

    user_ans = ''
    user_ans_variants = ['1', '2', '3']

    print('Что Вы хотели бы сделать:\n 1) Получить департаменты и их иерархию команд\n 2) Получить сводный отчет по '
          'департаментами\n 3) Сохранить сводный отчет в формате .csv')

    while user_ans not in user_ans_variants:
        print('Выберите: {}, {} или {}'.format(*user_ans_variants))
        user_ans = input()

    if user_ans == '1':
        get_hierarchy(departments)
    elif user_ans == '2':
        get_report(departments)
    else:
        save_report_to_csv(departments)
