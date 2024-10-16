import re
import pytest
import requests
from models import Post, Comment, Album, Photo, Todo, User


def test_get_post(base_url, status_code):
    response = requests.get(f'{base_url}/posts')
    assert response.status_code == status_code
    result = response.json()
    assert isinstance(result, list)
    assert len(result) == 100
    for post in result:
        assert Post.model_validate(post)


def test_get_post_by_id(base_url, status_code, post_id):
    response = requests.get(f'{base_url}/posts/{post_id}')
    assert response.status_code == status_code
    result = response.json()
    assert isinstance(result, dict)
    assert Post.model_validate(result)


def test_get_comment_post(base_url, status_code, post_id):
    response = requests.get(f'{base_url}/posts/{post_id}/comments')
    assert response.status_code == status_code
    result = response.json()
    assert isinstance(result, list)
    for comment in result:
        assert Comment.model_validate(comment)


def test_get_comment_by_post_id(base_url, status_code, post_id):
    response = requests.get(f'{base_url}/comments?postId={post_id}')
    assert response.status_code == status_code
    result = response.json()
    assert isinstance(result, list)
    for comment in result:
        assert Comment.model_validate(comment)     


def test_get_comments(base_url, status_code):
    response = requests.get(f'{base_url}/comments')
    assert response.status_code == status_code
    result = response.json()
    assert isinstance(result, list)
    assert len(result) == 500
    for comment in result:
        assert Comment.model_validate(comment)


def test_get_albums(base_url, status_code):
    response = requests.get(f'{base_url}/albums')
    assert response.status_code == status_code
    result = response.json()
    assert isinstance(result, list)
    assert len(result) == 100
    for album in result:
        assert Album.model_validate(album)


def test_get_photos(base_url, status_code, pattern_url_jsonplaceholder):
    response = requests.get(f'{base_url}/photos')
    assert response.status_code == status_code
    result = response.json()
    assert isinstance(result, list)
    assert len(result) == 5000
    for photo in result:
        assert Photo.model_validate(photo)
        assert re.match(pattern_url_jsonplaceholder, photo.get('url'))
        assert re.match(pattern_url_jsonplaceholder, photo.get('thumbnailUrl'))


@pytest.mark.json_debug
def test_get_todos(base_url, status_code):
    response = requests.get(f'{base_url}/todos')
    assert response.status_code == status_code
    result = response.json()
    assert len(result) == 200
    for todo in result:
        assert Todo.model_validate(todo)


def test_get_users(base_url, status_code):
    response = requests.get(f'{base_url}/users')
    assert response.status_code == status_code
    result = response.json()
    assert len(result) == 10
    for user in result:
        assert User.model_validate(user)


@pytest.mark.parametrize('num', range(1,5))
def test_post_posts(base_url, num):
    data = {'title': f'test_{num}', 'body': f'body_{num}', 'userId': 1}
    response = requests.post(url=f'{base_url}/posts', data=data)
    assert response.status_code == 201
    result = response.json()
    assert isinstance(result, dict)
    assert Post.model_validate(result)
    post_result = Post(**result)
    for key, value in data.items():
        assert getattr(post_result, key) == value


@pytest.mark.xfail(reason='Error "Cannot read properties of undefined (reading \'id\')"')
def test_put_posts(base_url, post_data):
    post_test = Post(**post_data)
    data = {'id':post_test.id, 'title': f'test_{post_test.body}', 'body': f'body_{post_test.title}', 'userId': post_test.userId}
    response = requests.put(url=f'{base_url}/posts/{post_test.id}', data=data)
    assert response.status_code == 202
    result = response.json()
    assert isinstance(result, dict)
    assert Post.model_validate(result)
    post_result = Post(**result)
    for key, value in data.items():
        assert getattr(post_result, key) == value


def test_patch_posts(base_url, status_code, post_data):
    post_test = Post(**post_data)
    data = {'title': f'test_{post_test.body}', 'body': f'body_{post_test.title}'}
    response = requests.patch(url=f'{base_url}/posts/{post_test.id}', data=data)
    assert response.status_code == status_code
    result = response.json()
    assert isinstance(result, dict)
    for key, value in result.items():
        assert data[key] == value


def test_delete_posts(base_url, status_code, post_data):
    post_test = Post(**post_data)
    response = requests.delete(url=f'{base_url}/posts/{post_test.id}')
    assert response.status_code == status_code
    check_delete = requests.get(url=f'{base_url}/posts/{post_test.id}')
    assert check_delete.status_code == 404
