import base64
from github import Github
from github import InputGitTreeElement
def Git_Push_Csv_File():
    g = Github(login_or_token='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')
    repo = g.get_user().get_repo('HostCsvForSnake')  # repo name
    file_list = [
        '.\\CsvForSnake.csv'
    ]
    file_names = [
        'CsvForSnake.csv'
    ]
    commit_message = 'python commit'
    master_ref = repo.get_git_ref('heads/main')
    master_sha = master_ref.object.sha
    base_tree = repo.get_git_tree(master_sha)

    element_list = list()
    for i, entry in enumerate(file_list):
        with open(entry) as input_file:
            data = input_file.read()
        if entry.endswith('.png'):  # images must be encoded
            data = base64.b64encode(data)
        element = InputGitTreeElement(file_names[i], '100644', 'blob', data)
        element_list.append(element)

    tree = repo.create_git_tree(element_list, base_tree)
    parent = repo.get_git_commit(master_sha)
    commit = repo.create_git_commit(commit_message, tree, [parent])
    master_ref.edit(commit.sha)
