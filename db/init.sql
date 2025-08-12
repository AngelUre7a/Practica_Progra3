-- Crear tabla clientes
CREATE TABLE clientes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre TEXT NOT NULL,
    email TEXT NOT NULL UNIQUE
);

-- Crear tabla compras
CREATE TABLE compras (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    cliente_id INTEGER NOT NULL,
    producto TEXT NOT NULL,
    cantidad INTEGER NOT NULL,
    fecha DATE NOT NULL,
    FOREIGN KEY(cliente_id) REFERENCES clientes(id)
);

-- Insertar clientes de prueba
INSERT INTO clientes (nombre, email) VALUES
('Juan Pérez', 'juan@example.com'),
('María López', 'maria@example.com'),
('Carlos Ruiz', 'carlos@example.com'),
('Ana Torres', 'ana@example.com'),
('Luis Gómez', 'luis@example.com'),
('Sofía Fernández', 'sofia@example.com'),
('Pedro Sánchez', 'pedro@example.com'),
('Lucía Díaz', 'lucia@example.com'),
('Miguel Castro', 'miguel@example.com'),
('Laura Martínez', 'laura@example.com');

-- Insertar compras de prueba
INSERT INTO compras (cliente_id, producto, cantidad, fecha) VALUES
(1, 'Laptop', 1, '2024-01-10'),
(2, 'Mouse', 2, '2024-02-15'),
(3, 'Teclado', 1, '2024-03-05'),
(4, 'Monitor', 1, '2024-03-20'),
(5, 'Auriculares', 1, '2024-04-12'),
(6, 'Impresora', 1, '2024-05-18'),
(7, 'Tablet', 1, '2024-06-22'),
(8, 'Smartphone', 1, '2024-07-30'),
(9, 'Cámara', 1, '2024-08-14'),
(10, 'Altavoces', 2, '2024-09-01');
