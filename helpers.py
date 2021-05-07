#pagination example usage
#throw error if no items and page is not 1
# if page is less than 1 or per_page is negative
#page or per_page are not ints
paginated_query = query.paginate(page, per_page)
total = paginated_query.total
paginated_query_items = paginated_query.items

#sample implementation here
https://github.com/pallets/flask-sqlalchemy/blob/2f4fd103321f27e7ab591ee27167a4e04fe593cc/src/flask_sqlalchemy/__init__.py
