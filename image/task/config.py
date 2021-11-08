# Database connection
database_name = "database"
database_user = "codetest"
database_password = "swordfish"
database_charset = "utf8"

uft_commands = ['SET NAMES utf8;', 'SET CHARACTER SET utf8;', 'SET character_set_connection=utf8;']

tables = {
    "peoples":
    """
    create table peoples (
	peoples_id integer auto_increment not null,
	given_name varchar(255) default null,
	family_name varchar(255) default null,
	date_of_birth DATE default null,
	place_of_birth varchar(255) default null,
    city_id int,
    primary key(peoples_id),
    constraint forkey_city foreign key(city_id) references city(city_id)
    )
    """
}

insert_tables = {
    "peoples":
    """
        INSERT ignore into peoples
        (peoples_id, given_name, family_name, date_of_birth, place_of_birth) 
        values (%s, %s, %s, %s, %s)
    """
}
main_query = """
    select peoples_id, given_name, family_name, date_of_birth, place_of_birth
    from peoples
    """
