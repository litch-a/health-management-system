from django.db import models
import uuid

class HealthProgram(models.Model):
    """Represents a health program or service offered."""
    program_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255, unique=True, help_text="Name of the health program (e.g., TB, Malaria, HIV).")
    description = models.TextField(blank=True, help_text="Optional description of the program.")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class Client(models.Model):
    """Represents a client registered in the system."""
    client_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    first_name = models.CharField(max_length=100, help_text="Client's first name.")
    last_name = models.CharField(max_length=100, help_text="Client's last name.")
    date_of_birth = models.DateField(null=True, blank=True, help_text="Client's date of birth.")
    gender = models.CharField(
        max_length=10,
        choices=[('Male', 'Male'), ('Female', 'Female'), ('Other', 'Other')],
        blank=True,
        help_text="Client's gender."
    )
    contact_number = models.CharField(max_length=20, blank=True, help_text="Client's contact phone number.")
    address = models.TextField(blank=True, help_text="Client's address.")
    registration_date = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class ClientEnrollment(models.Model):
    """Represents the enrollment of a client in a health program."""
    enrollment_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    client = models.ForeignKey(Client, on_delete=models.CASCADE, related_name='enrollments', help_text="Client enrolled in the program.")
    program = models.ForeignKey(HealthProgram, on_delete=models.CASCADE, help_text="Health program the client is enrolled in.")
    enrollment_date = models.DateTimeField(auto_now_add=True)
    notes = models.TextField(blank=True, help_text="Optional notes related to the enrollment.")

    class Meta:
        unique_together = ('client', 'program')  # Ensure a client can't be enrolled in the same program twice

    def __str__(self):
        return f"{self.client} enrolled in {self.program}"