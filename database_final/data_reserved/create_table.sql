-- 學生資料student_id,student_name,tel,address,school,grade,status
CREATE TABLE STUDENT (
    student_id VARCHAR(100) PRIMARY KEY,
    student_name VARCHAR(100) NOT NULL,
    tel VARCHAR(20),
    address VARCHAR(255),
    school VARCHAR(100),
    grade VARCHAR(50),
    status VARCHAR(50),
    -- parent_id INTEGER REFERENCES PARENT(parent_id) ON DELETE CASCADE
);

-- 家長資料
CREATE TABLE PARENT (
    parent_name VARCHAR(100) NOT NULL,
    parent_tel VARCHAR(20) NOT NULL,
    student_id REFERENCES STUDNET(student_id) ON DELETE CASCADE
);

-- 老師資料
CREATE TABLE TEACHER (
    teacher_id VARCHAR(20) PRIMARY KEY,
    teacher_name VARCHAR(100) NOT NULL,
    tel VARCHAR(20),
    address VARCHAR(255)
    status VARCHAR(20)
);

-- 課程資料
CREATE TABLE CLASS (
    class_id VARCHAR(10) PRIMARY KEY,
    class_name VARCHAR(100) NOT NULL,
    semester VARCHAR(20),
    time TIME,
    classroom_id REFERENCES CLASSROOM(classroom_id) ON DELETE SET NULL
);

-- 教室資料
CREATE TABLE CLASSROOM (
    classroom_id VARCHAR(20) PRIMARY KEY,
    classroom_name INT NOT NULL,
    capacity INTEGER NOT NULL
);

-- 輔導員資料
CREATE TABLE MENTOR (
    mentor_id INT PRIMARY KEY, 
    mentor_name VARCHAR(100) NOT NULL,
    tel VARCHAR(20),
    address VARCHAR(255),
    status VARCHAR(50)
);

-- 工作人員資料
CREATE TABLE WORKERS (
    worker_id VARCHAR(20) PRIMARY KEY,
    worker_name VARCHAR(100) NOT NULL,
    status VARCHAR(50),
    password VARCHAR(100)
);

-- 試聽資料
CREATE TABLE AUDIT (
    audit_id VARCHAR(100) PRIMARY KEY,
    audit_name VARCHAR(100) NOT NULL,
    school VARCHAR(100),
    grade VARCHAR(20),
    tel VARCHAR(20),
    address VARCHAR(255),
    status VARCHAR(50)
);

CREATE TABLE MENTOR_SHIFT (
    shift INT,
    mentor_id REFERENCES MENTOR(mentor_id) ON DELETE CASCADE
)

CREATE TABLE TAKE (
    student_id REFERENCES STUDENT(student_id) ON DELETE SET NULL,
    class_id REFERENCES CLASS(class_id) ON DELETE SET NULL
)

CREATE TABLE TEACH (
    teacher_id REFERENCES TEACHER(teacher_id) ON DELETE CASCADE,
    class_idREFERENCES CLASS(class_id) ON DELETE CASCADE
)