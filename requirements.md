# 🍄 MyMyco - Software Requirements Document

## 1. **Overview**
MyMyco is a fungal species management app that allows users to view, select, and manage mushroom species. Users can select existing species, add them to their personal collection (`MySpecies`), and create or modify custom species.

---

## 2. **Functional Requirements**

### 2.1 Species Management
- [FR-01] The system shall allow users to **search and browse** a pre-populated database of mushroom species.
- [FR-02] The system shall allow users to **add species** to their collection (`MySpecies`) via a `POST` request.
- [FR-03] The system shall allow users to **create custom species** via a `POST` to the `Species` model.
- [FR-04] The system shall automatically add a newly created custom species to `MySpecies`.

### 2.2 Custom Species Control
- [FR-05] The system shall only permit **PUT (edit) requests** on species marked as `is_custom=True`.
- [FR-06] The system shall disallow edits to non-custom (standard) species.

### 2.3 MySpecies Functionality
- [FR-07] The system shall store **added_at** timestamps for entries in `MySpecies`.
- [FR-08] The system shall support **soft-deletion** of species from `MySpecies` by setting `removed_at`.
- [FR-09] The system shall provide a filterable endpoint to show only active (`removed_at=None`) species.

---

## 3. **Non-Functional Requirements**

- [NFR-01] The system shall return search results in < 1 second for standard queries.
- [NFR-02] Only authenticated users (if login is added) shall be allowed to POST, PUT, or DELETE species.
- [NFR-03] The UI or API shall clearly distinguish between standard and custom species (e.g., by `is_custom` field).

---

## 4. **Business Rules**

- [BR-01] A `Species` instance created through the UI/API is marked with `is_custom=True`.
- [BR-02] A `Species` instance with `is_custom=False` must not be editable.
- [BR-03] Removing a species from `MySpecies` should not delete the related `Species` entry from the database.

---

## 5. **Data Models Summary**

### Species
- `scientific_name` (str)
- `is_custom` (bool, default=False)
- ... (other taxonomy/growth info fields)

### MySpecies
- `species` (FK to Species)
- `added_at` (datetime)
- `removed_at` (datetime, nullable)

---

## 6. **User Stories**

- As a grower, I want to select species from a master list so I can manage what I’m cultivating.
- As a grower, I want to create and track custom mushroom strains to experiment with new genetics.
- As a grower, I want to edit only my custom species so I don’t accidentally modify standard data.

---

Let me know if you'd like to expand this into a Markdown file, generate test cases, or link this to database design and serializers!