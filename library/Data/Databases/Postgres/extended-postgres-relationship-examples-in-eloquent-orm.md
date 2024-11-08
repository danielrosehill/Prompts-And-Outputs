---
title: "Extended Postgres Relationship Examples In Eloquent ORM"
---
![GPT-4o](https://img.shields.io/badge/GPT--4o-3333FF?style=for-the-badge&logo=openai&logoColor=white)



*Note: this repository consists of the outputs of large language models (LLMs). In many cases, these are unedited or minimally edited. The information provided is for demonstrative purposes only and is intended to highlight constraints and capabilities in LLM applications and prompt engineering strategies.*


Certainly! Here’s a comprehensive guide with examples for each type of relationship using the Output Hub project as context.

### **1. One-to-Many (M2O) Relationship**

**Scenario:**
A `CustomGpt` configuration can have multiple `PromptLibrary` entries, but each `PromptLibrary` entry belongs to one `CustomGpt`.

**Eloquent Implementation:**

- **In the `CustomGpt` Model:**
  ```php
  public function promptLibraries()
  {
      return $this->hasMany(PromptLibrary::class);
  }
  ```

  - **Explanation:** 
    - The `hasMany` method indicates that one `CustomGpt` can be associated with multiple `PromptLibrary` entries.

- **In the `PromptLibrary` Model:**
  ```php
  public function customGpt()
  {
      return $this->belongsTo(CustomGpt::class);
  }
  ```

  - **Explanation:**
    - The `belongsTo` method indicates that each `PromptLibrary` entry belongs to one `CustomGpt`.

**Database Schema:**
- The `prompt_libraries` table will have a `custom_gpt_id` column to establish this relationship.

---

### **2. Many-to-One (O2M) Relationship**

**Scenario:**
Each `PromptLibrary` entry can be associated with multiple `PromptOutputs`, but each `PromptOutput` belongs to one `PromptLibrary`.

**Eloquent Implementation:**

- **In the `PromptLibrary` Model:**
  ```php
  public function promptOutputs()
  {
      return $this->hasMany(PromptOutput::class);
  }
  ```

  - **Explanation:** 
    - The `hasMany` method indicates that one `PromptLibrary` entry can have many associated `PromptOutputs`.

- **In the `PromptOutput` Model:**
  ```php
  public function promptLibrary()
  {
      return $this->belongsTo(PromptLibrary::class);
  }
  ```

  - **Explanation:**
    - The `belongsTo` method indicates that each `PromptOutput` belongs to one `PromptLibrary`.

**Database Schema:**
- The `prompt_outputs` table will have a `prompt_library_id` column to establish this relationship.

---

### **3. Many-to-Many (M2M) Relationship**

**Scenario:**
A `PromptOutput` can be associated with multiple `PromptLibrary` entries, and each `PromptLibrary` entry can be associated with multiple `PromptOutputs`.

**Eloquent Implementation:**

- **In the `PromptOutput` Model:**
  ```php
  public function promptLibraries()
  {
      return $this->belongsToMany(PromptLibrary::class, 'prompt_outputs_prompt_library');
  }
  ```

  - **Explanation:** 
    - The `belongsToMany` method indicates that this model is related to many instances of another model, and vice versa. The second parameter specifies the name of the pivot table that manages this relationship.

- **In the `PromptLibrary` Model:**
  ```php
  public function promptOutputs()
  {
      return $this->belongsToMany(PromptOutput::class, 'prompt_outputs_prompt_library');
  }
  ```

  - **Explanation:**
    - This method in the `PromptLibrary` model defines the Many-to-Many relationship in the opposite direction.

**Database Schema:**
- A junction (or pivot) table named `prompt_outputs_prompt_library` is required. This table contains two foreign keys:
  - `prompt_output_id`: References the `id` in the `prompt_outputs` table.
  - `prompt_library_id`: References the `id` in the `prompt_library` table.

**Junction Table Example:**
```php
use Illuminate\Database\Eloquent\Relations\Pivot;

class PromptOutputsPromptLibrary extends Pivot
{
    protected $table = 'prompt_outputs_prompt_library';

    protected $fillable = ['prompt_output_id', 'prompt_library_id'];
}
```

---

### **4. One-to-One (O2O) Relationship**

**Scenario:**
Each `User` can have one and only one `UserProfile`, and each `UserProfile` belongs to one and only one `User`.

**Eloquent Implementation:**

- **In the `User` Model:**
  ```php
  public function profile()
  {
      return $this->hasOne(UserProfile::class);
  }
  ```

  - **Explanation:** 
    - The `hasOne` method indicates that each `User` can have one `UserProfile`.

- **In the `UserProfile` Model:**
  ```php
  public function user()
  {
      return $this->belongsTo(User::class);
  }
  ```

  - **Explanation:**
    - The `belongsTo` method indicates that each `UserProfile` belongs to one `User`.

**Database Schema:**
- The `user_profiles` table will have a `user_id` column with a unique constraint to ensure the one-to-one relationship.

---

### **5. Zero-to-Many (Z2M) Relationship**

**Scenario:**
A `CustomGpt` configuration may have multiple associated `ApiKeys`, but a `CustomGpt` might also have zero `ApiKeys`.

**Eloquent Implementation:**

- **In the `CustomGpt` Model:**
  ```php
  public function apiKeys()
  {
      return $this->hasMany(ApiKey::class);
  }
  ```

  - **Explanation:** 
    - The `hasMany` method indicates that a `CustomGpt` can have zero or many `ApiKeys`.

- **In the `ApiKey` Model:**
  ```php
  public function customGpt()
  {
      return $this->belongsTo(CustomGpt::class);
  }
  ```

  - **Explanation:**
    - The `belongsTo` method indicates that each `ApiKey` belongs to one `CustomGpt`.

**Database Schema:**
- The `api_keys` table will have a `custom_gpt_id` column, which may be null if no API keys are associated.

---

### **6. Zero-to-One (Z2O) Relationship**

**Scenario:**
A `PromptOutput` might have an associated `Review`, but it’s possible that some outputs have not been reviewed yet, meaning the relationship might not exist.

**Eloquent Implementation:**

- **In the `PromptOutput` Model:**
  ```php
  public function review()
  {
      return $this->hasOne(Review::class);
  }
  ```

  - **Explanation:** 
    - The `hasOne` method indicates that a `PromptOutput` may have zero or one `Review`.

- **In the `Review` Model:**
  ```php
  public function promptOutput()
  {
      return $this->belongsTo(PromptOutput::class);
  }
  ```

  - **Explanation:**
    - The `belongsTo` method indicates that a `Review` belongs to one `PromptOutput`.

**Database Schema:**
- The `reviews` table will have a `prompt_output_id` column, which may be null if the review does not exist yet.

---

### Summary of All Relationships in Eloquent

Here’s a summary of the relationships with corresponding Eloquent methods:

#### **One-to-Many (M2O)**
- **Model A (One Side)**: `hasMany(ModelB::class)`
- **Model B (Many Side)**: `belongsTo(ModelA::class)`

#### **Many-to-One (O2M)**
- **Model A (Many Side)**: `belongsTo(ModelB::class)`
- **Model B (One Side)**: `hasMany(ModelA::class)`

#### **Many-to-Many (M2M)**
- **Model A**: `belongsToMany(ModelB::class, 'pivot_table')`
- **Model B**: `belongsToMany(ModelA::class, 'pivot_table')`

#### **One-to-One (O2O)**
- **Model A**: `hasOne(ModelB::class)`
- **Model B**: `belongsTo(ModelA::class)`

#### **Zero-to-Many (Z2M)**
- **Model A**: `hasMany(ModelB::class)`
- **Model B**: `belongsTo(ModelA::class)`

#### **Zero-to-One (Z2O)**
- **Model A**: `hasOne(ModelB::class)`
- **Model B**: `belongsTo(ModelA::class)`

---

### Example Implementation for Output Hub Project

```php
use Illuminate\Database\Eloquent\Model;

// CustomGpt Model
class CustomGpt extends Model
{
    protected $fillable = ['gpt_name', 'description', 'user_id'];

    public function promptLibraries()
    {
        return $this->hasMany(PromptLibrary::class);
    }

    public function apiKeys()
    {
        return $this->hasMany(ApiKey::class);
    }
}

// PromptLibrary Model
class PromptLibrary extends Model
{
    protected $fillable = ['prompt_text', 'summary', 'rating', 'display_in_library'];

    public function promptOutputs()
    {
        return $this->hasMany(PromptOutput::class);
    }

    public function customGpt()
    {
        return $->belongsTo(CustomGpt::class);
    }

    public function promptOutputs()
    {
        return $this->belongsToMany(PromptOutput::class, 'prompt_outputs_prompt_library');
    }
}

// PromptOutput Model
class PromptOutput extends Model
{
    protected $fillable = ['output_text', 'accuracy_assessment_id', 'review_urgency_id', 'prompt_library_id'];

    public function promptLibrary()
    {
        return $this->belongsTo

(PromptLibrary::class);
    }

    public function promptLibraries()
    {
        return $this->belongsToMany(PromptLibrary::class, 'prompt_outputs_prompt_library');
    }

    public function review()
    {
        return $this->hasOne(Review::class);
    }
}

// Review Model
class Review extends Model
{
    protected $fillable = ['review_text', 'prompt_output_id'];

    public function promptOutput()
    {
        return $this->belongsTo(PromptOutput::class);
    }
}

// ApiKey Model
class ApiKey extends Model
{
    protected $fillable = ['api_key', 'custom_gpt_id'];

    public function customGpt()
    {
        return $this->belongsTo(CustomGpt::class);
    }
}

// PromptOutputsPromptLibrary Junction Table
use Illuminate\Database\Eloquent\Relations\Pivot;

class PromptOutputsPromptLibrary extends Pivot
{
    protected $table = 'prompt_outputs_prompt_library';

    protected $fillable = ['prompt_output_id', 'prompt_library_id'];
}
```

This comprehensive guide should give you a complete understanding of how to define various types of relationships using Eloquent ORM in the context of your Output Hub project.