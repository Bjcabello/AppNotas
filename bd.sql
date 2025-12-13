-- Crear base de datos si no existe
IF NOT EXISTS (SELECT name FROM sys.databases WHERE name = 'DBNOTA')
BEGIN
    CREATE DATABASE DBNOTA;
END;
GO

USE DBNOTA;
GO

CREATE TABLE usuarios(
    id INT IDENTITY(1,1) NOT NULL,
    nombre VARCHAR(180),
    apellidos VARCHAR(255),
    email VARCHAR(255) NOT NULL,
    password VARCHAR(255) NOT NULL,
    fecha DATE NOT NULL,
    CONSTRAINT pk_usuarios PRIMARY KEY(id),
    CONSTRAINT uq_email UNIQUE(email)
);
GO

CREATE TABLE notas(
    id INT IDENTITY(1,1) NOT NULL,
    usuario_id INT NOT NULL,
    titulo VARCHAR(255) NOT NULL,
    descripcion VARCHAR(MAX)
    fecha DATE NOT NULL,
    CONSTRAINT pk_notas PRIMARY KEY(id),
    CONSTRAINT fk_notas_usuarios FOREIGN KEY(usuario_id) REFERENCES usuarios(id)
);
GO
